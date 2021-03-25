import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Utility Commands"""

    @commands.Cog.listener()
    async def on_ready(self):
         print('Utils ✅') 

#GUILD MANAGEMENT-----------------------------------------------------------
    @commands.command(aliases=["slowmode"])
    @has_permissions(manage_channels=True)
    async def setdelay(self, ctx, seconds: int):
        """Changes Channel Slowmode)"""
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds}s!") 
    @commands.command(aliases=["lock"])
    @commands.has_permissions(manage_channels = True) 
    async def silence(self, ctx, channel : discord.TextChannel=None):
        """Locks Channel (@everyone role only!)"""
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        embed = discord.Embed(description=f"<:smileSucess:786890205993893908> This channel has been locked!", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command(aliases=["unlock"])
    @commands.has_permissions(manage_channels = True) 
    async def unsilence(self, ctx, channel : discord.TextChannel=None):
        """Unlocks Channel (@everyone role only!)"""
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        embed = discord.Embed(description=f"<:smileSucess:786890205993893908> This channel has been unlocked!", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=20):
        """Purges Messages"""
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.author.mention} has purged {amount}")
    @commands.command()
    @commands.has_permissions(manage_channels = True) 
    async def ccategory(self, ctx, *, name):
        """creates a category"""
        await ctx.guild.create_category(name)
        embed = discord.Embed(description=f"<:smileSucess:786890205993893908> Sucessfully made category", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_channels = True) 
    async def cchannel(self, ctx, *, name):
        """creates a channel"""
        await ctx.guild.create_text_channel(name)
        await ctx.guild.create_category(name)
        embed = discord.Embed(description=f"<:smileSucess:786890205993893908> Sucessfully made channel", color=0x43b581)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utility(client))
