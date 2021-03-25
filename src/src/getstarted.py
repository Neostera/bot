import discord
import random
from discord.ext import commands

class GetStarted(commands.Cog):
    def __init__(self, client):
        self.client = client
    """Help Commands"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Start COmmands ✅')
         
    @commands.command(aliases=['perms'])
    async def permissions(self, ctx, member: discord.Member = None):
        """Shows needed permissions for channels"""
        e = discord.Embed(title="Channel Permissions Required (@everyone)", color = 0xff0000)
        e.add_field(name="__General Channel Permissions__", value="_ _", inline=False)
        e.add_field(name="View Channel", value="<:redtick:805007407038070804>", inline=True)
        e.add_field(name="Manage Channel", value="<:redtick:805007407038070804>", inline=True)
        e.add_field(name="Manage Permissions", value="<:redtick:805007407038070804>", inline=True)
        e.add_field(name="Manage Webhooks", value="<:redtick:805007407038070804>", inline=True)
        e.add_field(name="__Membership Permissions__", value="_ _", inline=False)
        e.add_field(name="Send Messages", value="<:greentick:805007406663860265>", inline=True)
        e.add_field(name="If you want something like a ""Verified Role"", just <:greentick:805007406663860265>\
View Channel, then leave everything neutral (<:neutral:805006562699640884>) ", value="<:greentick:805007406663860265>", inline=True)
        e.add_field(name="__Below These Can Be Anything You Want!__", value="We use these perms (ˇ) in the image below", inline=False)
        e.set_image(url=f"https://media.discordapp.net/attachments/803575524659560458/805020648086700082/unknown.png?width=480&height=406")
        await ctx.send(embed=e)
    @commands.command()
    @commands.has_permissions(manage_channels = True) 
    async def setup(self, ctx, channel : discord.TextChannel=None):
        """Setups @everyone permissions! (Do this in each channel lol)"""
        category = category or ctx.category
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = True
        await category.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        embed = discord.Embed(description=f"<:smileSucess:786890205993893908> Succesfully updates permissions!", color=0x43b581)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(GetStarted(client))
