import discord
import json
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, ConversionError
from discord.ext.commands.cooldowns import BucketType
from time import sleep
from pretty_help import PrettyHelp


#PREFIX
def get_prefix(client, message):
  with open('json/prefixes.json', 'r') as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix, help_command=PrettyHelp())
client._BotBase__cogs = commands.core._CaseInsensitiveDict()
@client.event
async def on_guild_join(guild):
    with open('json/prefixes.json', 'r') as f:
      prefixes = json.load(f)
    prefixes[str(guild.id)] = 'b,'
    with open('json/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)
@client.event
async def on_guild_remove(guild):
      with open('json/prefixes.json', 'r') as f:
        prefixes = json.load(f)
      prefixes.pop(str(guild.id))
      with open('json/prefixes.json', 'w') as f:
       json.dump(prefixes, f, indent=4)
@client.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
      with open('json/prefixes.json', 'r') as f:
        prefixes = json.load(f)
      prefixes[str(ctx.guild.id)] = prefix
      with open('json/prefixes.json', 'w') as f:
       json.dump(prefixes, f, indent=4)
      await ctx.send('Prefix has been changed to: '+ str(prefix))
#COGS---------------------------------------------
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'src.{extension}')

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'src.{extension}')

for filename in os.listdir('./src'):
    if filename.endswith('.py'):
         client.load_extension(f'src.{filename[:-3]}')
  
#EVENT
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed = discord.Embed(title="<:smileError:789427521124171776> Thou art missing p'rmission(s) to runneth this command!", color=0xff0000)
        await ctx.send(embed=embed)
    else:
        raise error

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Activity, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
  
#snipe---------------------------------------------------------------------------------
snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     #await sleep(1)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(title = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=0xff0000)
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

client.run(';-;')
