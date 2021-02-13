import discord
import random
import aiohttp
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Bible(commands.Cog):
    def __init__(self, client):
        self.client = client
    """List of Biblical commands!"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Bible ✅')

    @commands.command()
    async def bible(self, ctx):
        """Random Bible Verse"""
        embed = discord.Embed(color=0xe74c3c)
        embed.set_image(url=f"https://dailyverses.net/random-bible-verse-picture")
        await ctx.send(embed=embed)
    @commands.command()
    async def biblee(self, msg):
     """Random Bible Verse"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://dailyverses.net/random-bible-verse-picture') as bible:
             bible = await bible.json()
             return await msg.channel.send(bible['url'])
def setup(client):
    client.add_cog(Bible(client))

