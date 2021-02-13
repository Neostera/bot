import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class OnlyOwner(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
         print('Only Owner ✅')

    @commands.command(hidden=True)
    @commands.has_permissions(ban_members=True)
    async def bans(self, ctx, member: discord.Member, *, reason=None):
        """Bans a user | Oh Yes, Owner Also has Power"""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(hidden=True)
    @commands.has_permissions(kick_members=True)
    async def kicks(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a user | Oh Yes, Owner Also has Power"""
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')
   
    @commands.command(hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def clears(self, ctx, amount=20):
        """Purges Amount of Messages | Oh Yes, Owner Also has Power"""
        await ctx.channel.purge(limit=amount)
        await ctx.send("Refreshing channel")
#GUILDS
    @commands.command(hidden=True)
    async def servers(self, ctx):
        activeservers = client.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)

def setup(client):
    client.add_cog(OnlyOwner(client))
