import discord
import aiohttp
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Modules(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Help Commands"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Help Commands ✅')
         
    @commands.command()
    async def commands(self, ctx):
        e = discord.Embed(title=":books: Help", color=0xff0000)
        e.add_field(name=":hammer: Moderation", value=f"`,help mod`\nClick for more info")
        e.add_field(name="<:smileManage:789773787557134337> Utilities", value=f"`,help utils`\nClick for more info")
        e.add_field(name="<:smileFun:789781188780228608> Fun", value=f"`,help fun`\nClick for more info")
        e.add_field(name=":camera: Images", value=f"`,help img`\nClick for more info")
        e.add_field(name="<:smileDog:789779044052107294> Animals", value=f"`,help animals`\nClick for more info")
        e.add_field(name="<:bible:790504604215279636> Bible", value=f"`,help bible`\nClick for more info")
        e.add_field(name=":information_source: Info & Get Started", value=f"`,help info`\nClick for more info")
        await ctx.send(embed=e)

def setup(client):
    client.add_cog(Modules(client))
