import discord
import aiohttp
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Animals(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Animal Commands"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Animals ✅')
         
    @commands.command()
    async def cat(self, msg):
     """Random Fox Image"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://aws.random.cat/meow') as cat:
             cat = await cat.json()
             return await msg.channel.send(cat['file'])
    @commands.command()
    async def dog(self, msg):
     """Random Dog Image"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://dog.ceo/api/breeds/image/random') as dog:
             dog = await dog.json()
             return await msg.channel.send(dog['message'])        
    @commands.command()
    async def lizard(self, msg):
     """Random Lizard Image"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://nekos.life/api/lizard') as lizard:
             lizard = await lizard.json()
             return await msg.channel.send(lizard['url'])
    @commands.command()
    async def duck(self, msg):
     """Random Duck Image"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://random-d.uk/api/v1/random') as duck:
             duck = await duck.json()
             return await msg.channel.send(duck['url'])
    @commands.command()
    async def fox(self, ctx):
     """Random Fox Image"""
     async with aiohttp.ClientSession() as req:
         async with req.get('https://randomfox.ca/floof') as fox:
             fox = await fox.json()
             return await ctx.channel.send(fox['image'])
def setup(client):
    client.add_cog(Animals(client))
