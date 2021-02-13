import discord
import aiohttp
import asyncio
import os
import cogs
import json
import random
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, ConversionError
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands.cooldowns import BucketType
from time import sleep

#PREFIX
def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix)
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
    prefixes[str(guild.id)] = ','
    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)
@client.event
async def on_guild_remove(guild):
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
      prefixes.pop(str(guild.id))
      with open('prefixes.json', 'w') as f:
       json.dump(prefixes, f, indent=4)
@client.command()
@commands.has_permissions(administrator = True)
async def prefix_set(ctx, prefix):
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
      prefixes[str(ctx.guild.id)] = prefix
      with open('prefixes.json', 'w') as f:
       json.dump(prefixes, f, indent=4)
      await ctx.send('Prefix has been changed to: '+ str(prefix))
@client.command(pass_context=True) 
async def prefix(ctx):
    e = discord.Embed(title="Prefix", description="Prefixes are used before commands!", color=0xff0000)
    e.add_field(name="Set Prefix", value="`,prefix set <prefix>`", inline=True)
    await ctx.send(embed=e)
    
#HELP COMMAND----------------------------
cog = client.get_cog("moderation")
cog = client.get_cog("animals")
cog = client.get_cog("bible")
cog = client.get_cog("fun")
cog = client.get_cog("img")
cog = client.get_cog("imggeneration")
cog = client.get_cog("info")
cog = client.get_cog("misc")
cog = client.get_cog("modules")
cog = client.get_cog("onlyowner")
cog = client.get_cog("start")
cog = client.get_cog("utils")

class newhelp(commands.HelpCommand):
    async def send_client_help(self, mapping):
        embed = discord.Embed(title="Help", color=0xfffffe)
        for cog, commands in mapping.items():
           command_signatures = [self.get_command_signature(c) for c in commands]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value=", ".join(command_signatures), inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)
        
class newhelp(commands.MinimalHelpCommand):
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command), color=0xfffffe)
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)
        
class newhelp(commands.HelpCommand):
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", value=error, color=0xfffffe)
        channel = self.get_destination()
        await channel.send(embed=embed)
        
class newhelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        raise commands.BadArgument("An Error Occured")
    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Error", description=str(error), color=0xfffffe)
            await ctx.send(embed=embed)
        else:
            raise error
        
client.help_command = newhelp()
client._BotBase__cogs = commands.core._CaseInsensitiveDict()

#COGS---------------------------------------------
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
         client.load_extension(f'commands.{filename[:-3]}')

#SERVERSETUP
@client.command(hidden=True)
@commands.is_owner()
async def verify(ctx):
    emby = discord.Embed(title=f"Authentication Needed", description="Please Click/Tap the Reaction below to prove you are human.\
This will give you access to the **server**.", color=0xfffffe)
    await ctx.send(embed=emby)
@client.command(hidden=True)
@commands.is_owner()
async def nitro(ctx):
    await ctx.send("https://discordgift.site/c/uZVX2woVfUzf5AJu")
  
#EVENT
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed = discord.Embed(title="<:smileError:789427521124171776> Thou art missing p'rmission(s) to runneth this command!", color=0xff0000)
        await ctx.send(embed=embed)
    else:
        raise error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, prithee tryeth again in {:.2f}s'.format(error.retry_after)
        embed = discord.Embed(title='<:smileError:789427521124171776>This command is ratelimited, prithee tryeth again in {:.2f}s'.format(error.retry_after), color=0xff0000)
        await ctx.send(embed=embed)
    else:
        raise error
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #await client.change_presence(status=discord.Activity, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers! | ,help"))
    
#Logging--------------------------------------------------
#snipe
snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     #await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", title="Sniped!", description = snipe_message_content[channel.id], color=0xff0000)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"```diff\n-There are no recently deleted messages in #{channel.name}!```")

#gatekeeper-------------------------------
@client.event
async def on_member_join(member):
    emby = discord.Embed(title=f"{member.name} ({{member.id}}) has joined!", color=0x43b581)
    emby.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    channel=client.get_channel(803575442224971797)
    await ctx.send(embed=embed)
@client.event
async def on_member_remove(member):
    emby = discord.Embed(title=f"{member.name} ({{member.id}}) has left...", color=0x43b581)
    emby.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    #channel=client.get_channel(803575442224971797)
    await client.get_channel(803575442224971797).send(embed=emby)


client.run('NzQyNjYwMjU4MTI3Njc1NDQy.XzJWQw.HwU5rVPdHtxIAJPoBeovX3nLZgM')
