import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Image Commands"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Images ✅')
#AVATAR-RELATED--------------------------------------------------------------------------------------------------
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *,  member : discord.Member=None):
        """Shows User's Avatar (Mention/ID)"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url
        embed = discord.Embed(title="Avatar", color=0xe74c3c)
        embed.set_image(url=f"{userAvatarUrl}")
        await ctx.send(embed=embed)

    #User AVatar-------------------------------------------------------
    @commands.command()
    async def drip(self, ctx, *,  member : discord.Member=None):
        """be cool"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="drip", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/drip?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def firsttime(self, ctx, *,  member : discord.Member=None):
        """james franco ballad of buster scruggs"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="first time :O", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def grave(self, ctx, *,  member : discord.Member=None):
        """ded"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="rip", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/grave?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def heaven(self, ctx, *,  member : discord.Member=None):
        """*athereal music playing*"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="heaven", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/heaven?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def stonks(self, ctx, *,  member : discord.Member=None):
        """stonks"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="stonks", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/stonks?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def tableflip(self, ctx, *,  member : discord.Member=None):
        """tableflip someone"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="tableflip", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/tableflip?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def wolverine(self, ctx, *,  member : discord.Member=None):
        """wolverine"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="wolverine likes you", color=0xe74c3c)
        embed.set_image(url=f"https://vacefron.nl/api/wolverine?user={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def trash(self, ctx, *,  member : discord.Member=None):
        """somebody going to trash"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="trash execution", color=0xe74c3c)
        embed.set_image(url=f"https://api.no-api-key.com/api/v2/trash/?image={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def gay(self, ctx, *,  member : discord.Member=None):
        """rainbow overlay"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="gae", color=0xe74c3c)
        embed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def trigger(self, ctx, *,  member : discord.Member=None):
        """triggers somebody"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="triggered", color=0xe74c3c)
        embed.set_image(url=f"https://some-random-api.ml/canvas/triggered?avatar={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def wasted(self, ctx, *,  member : discord.Member=None):
        """gta wasted"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="wasted", color=0xe74c3c)
        embed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={userAvatarUrl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def wanted(self, ctx, *,  member : discord.Member=None):
        """wanted in the west"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        userAvatarUrl = member.avatar_url_as(static_format='png')
        embed = discord.Embed(title="wanted", color=0xe74c3c)
        percent = random.randint(1, 3)
        embed.set_image(url=f"https://api.xzusfin.repl.co/wanted?image={userAvatarUrl}&style={percent}")
        await ctx.send(embed=embed)
#AV AND TEXT----------------------------------------------------------------------------------
    @commands.command()
    async def yt(self, ctx, text):
        """imagine getting 2k likes is yt"""
        userAvatarUrl = member.avatar_url
        embed = discord.Embed(title="youtube", color=0xe74c3c)
        embed.set_image(url=f"https://some-random-api.ml/canvas/youtube-comment?avatar={userAvatarUrl}&username={self.ctx.author}&comment={text}")
        await ctx.send(embed=embed)
#OTHER-------------------------------------------------------------------------------------
    @commands.command()
    async def weather(self, ctx, *, text):
        """checks weather"""
        embed = discord.Embed(title=f"Weather in {text}", color=0xe74c3c)
        embed.set_image(url=f"https://wttr.in/{text}.png?m")
        await ctx.send(embed=embed)
#MEMEssss-------------------------------------------------------------------------------
    @commands.command()
    async def meme(self, ctx):
        """Random Meme"""
        percent = random.randrange(490)
        embed = discord.Embed(title="Meme", color=0xe74c3c)
        embed.set_image(url=f"https://ctk-api.herokuapp.com/meme/{percent}")
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Images(client))
