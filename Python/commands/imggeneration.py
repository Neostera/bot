import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class ImageGeneration(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Image Commands"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Image Generation ✅')
        
    @commands.command()
    async def rickify(self, ctx, *, text):
        """rickifies a message"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="Rickified", color=0xe74c3c)
        embed.set_image(url=f"https://xackbonu.sirv.com/Screenshot_20201228_172556.jpg?text.0.text={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def qr(self, ctx, *, text):
        """qr-ifies a message"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="qr code", color=0xe74c3c)
        embed.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def trumpify(self, ctx, *, text):
        """trump go tweet"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="Trumpified", color=0xe74c3c)
        embed.set_image(url=f"https://api.no-api-key.com/api/v2/trump?message={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def cmm(self, ctx, *, text):
        """change my mind"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="Change My Mind", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/changemymind?text={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def carreverse(self, ctx, *, text):
        """car reverse meme"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="Car Reverse", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/carreverse?text={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def emergency(self, ctx, *, text):
        """emergency meeting meme"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="Emergency Meeting", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/emergencymeeting?text={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def water(self, ctx, *, text):
        """water"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="gimme water", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/water?text={ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def cattalk(self, ctx, *, text):
        """cat talks what you want"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="cat go meow", color=0xe74c3c)
        embed.set_image(url=f"https://cataas.com/cat/says/{ftext}")
        await ctx.send(embed=embed)
    @commands.command()
    async def captcha(self, ctx, *, text):
        """captcha-like image"""
        ftext = text.replace(" ", "+") 
        embed = discord.Embed(title="verify", color=0xe74c3c)
        embed.set_image(url=f"https://api.no-api-key.com/api/v2/recaptcha?text={ftext}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ImageGeneration(client))