import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client
    """List of Bot INfo commands!"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Info ✅')
        
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=":ping_pong: ```Pong!```", color=0xff0000)
        embed.set_image(url=f"https://dummyimage.com/200x120/f04747/000000.png&text=+{round(self.client.latency * 1000)}ms")
        await ctx.send(embed=embed)
    @commands.command(aliases=['invite', 'support', 'server', 'website'])
    async def links(self, ctx):
        embed = discord.Embed(title=":link: Links", color=0xff0000)
        embed.add_field(name="Add Me", value="[Click Me](https://discord.com/api/oauth2/authorize?client_id=742660258127675442&permissions=8&scope=bot)", inline=True)
        embed.add_field(name="Smile Development ", value="[Click Me](https://discord.gg/kz2ab6RRuk)", inline=True)
        embed.add_field(name="Smile Community", value="[Click Me](https://discord.gg/F9wKsPYkM8)", inline=True)
        embed.add_field(name="Stratobot Support", value="[Click Me](https://discord.gg/r68fjuqPpX)", inline=True)
        embed.add_field(name="Website", value="[Click Me](https://stratobot.github.io/)", inline=True)
        await ctx.send(embed=embed)
    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        """Shows Bot Information"""
        embedVar = discord.Embed(title="A.I. Information", description="I am Stratobot,\
 a multipurpose Discord Bot", color=0xff0000)
        embedVar.set_thumbnail(url="https://lcc.yccd.edu/wp-content/themes/LCC/_img/icons/icon-information.png")
        embedVar.add_field(name="Creator:", value="[AirSupplierSs#7093](https://discord.com/users/729216428829442069)", inline=False)
        embedVar.add_field(name="Language:", value="<:python:805007406974369822> [Python](https://en.wikipedia.org/wiki/Python_(programming_language))", inline=False)
        embedVar.add_field(name="Latency:", value=f"`{round(self.client.latency * 1000)}ms`", inline=False)
        embedVar.add_field(name="Servers:", value=f"`{len(self.client.guilds)}`", inline=False)
        await ctx.send(embed=embedVar)
    @commands.command(aliases=['servercount'])
    async def servers(self, ctx):
        """Shows How Many Servers The Bot is In"""
        embedVar.add_field(name="Servers:", value=f"`{len(self.client.guilds)}`", inline=False)
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Information(client))
