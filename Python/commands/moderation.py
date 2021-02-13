import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, ConversionError

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Moderation Commands"""
        
    @commands.Cog.listener()
    async def on_ready(self):
         print('Moderation ✅')  
#USER
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a user"""
        await member.kick(reason=reason)
        embed = discord.Embed(description=f"<:greentick:805007406663860265> ***{member.mention} has been kicked*** | {reason}", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a user"""
        await member.ban(reason=reason)
        embed = discord.Embed(description=f"<:greentick:805007406663860265> ***{member.mention} has been banned*** | {reason}", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_nicknames=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nick(self, ctx, member: discord.Member, nick):
        """Change someone's nickname"""
        await member.edit(nick=nick)
        embed = discord.Embed(description=f"<:greentick:805007406663860265> ***Nickname was changed for {member.mention}!***", color=0x43b581)
        await ctx.send(embed=embed)
#ROLES
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def rank(self, ctx, user: discord.Member, role: discord.Role):
        """Gives a role (ranking users)"""
        await user.add_roles(role)
        embed = discord.Embed(description=f"<:greentick:805007406663860265> ***{ctx.author.mention}, {user.mention} has obtained a role called {role.name}***", color=0x43b581)
        await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def derank(self, ctx, user: discord.Member, role: discord.Role):
        """Removes a role (deranking users)"""
        await user.remove_roles(role)
        embed = discord.Embed(description=f"<:greentick:805007406663860265> ***{ctx.author.mention}, {user.mention} has lost a role called {role.name}***", color=0x43b581)
        await ctx.send(embed=embed)
#ERRORS_---------------------------------------------------------------------------------------------------------------------------
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Kick Command")
            embed.add_field(name="Usage:", value=",kick [user] [reason]", inline=False)
            embed.add_field(name="Example:", value=",kick @SuperTrouper too cool", inline=False)
            await ctx.send(embed=embed)
        else:
            raise error
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Ban Command")
            embed.add_field(name="Usage:", value=",ban [user] [reason]", inline=False)
            embed.add_field(name="Example:", value=",ban @SuperTrouper too cool", inline=False)
            await ctx.send(embed=embed)
        else:
            raise error
    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Nick Command")
            embed.add_field(name="Usage:", value=",nick [user] [nickname]", inline=False)
            embed.add_field(name="Example:", value=",nick @SuperTrouper noice", inline=False)
            await ctx.send(embed=embed)
        else:
            raise error
    
def setup(client):
    client.add_cog(Moderation(client))
