import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Ifiers(commands.Cog):
    def __init__(self, client):
        self.client = client
    """List of Ify commands!"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Ifiers ✅') 

    @commands.command()
    async def emojify(self, ctx, *, text):
        """emojifies your text"""
        text = text.replace("a", ":regional_indicator_a:")
        text = text.replace("b", ":regional_indicator_b:")
        text = text.replace("c", ":regional_indicator_c:")
        text = text.replace("d", ":regional_indicator_d:")
        text = text.replace("e", ":regional_indicator_e:")
        text = text.replace("f", ":regional_indicator_f:")
        text = text.replace("g", ":regional_indicator_g:")
        text = text.replace("h", ":regional_indicator_h:")
        text = text.replace("i", ":regional_indicator_i:")
        text = text.replace("j", ":regional_indicator_j:")
        text = text.replace("k", ":regional_indicator_k:")
        text = text.replace("l", ":regional_indicator_l:")
        text = text.replace("m", ":regional_indicator_m:")
        text = text.replace("n", ":regional_indicator_n:")
        text = text.replace("o", ":regional_indicator_o:")
        text = text.replace("p", ":regional_indicator_p:")
        text = text.replace("q", ":regional_indicator_q:")
        text = text.replace("r", ":regional_indicator_r:")
        text = text.replace("s", ":regional_indicator_s:")
        text = text.replace("t", ":regional_indicator_t:")
        text = text.replace("u", ":regional_indicator_u:")
        text = text.replace("v", ":regional_indicator_v:")
        text = text.replace("w", ":regional_indicator_w:")
        text = text.replace("x", ":regional_indicator_x:")
        text = text.replace("y", ":regional_indicator_y:")
        text = text.replace("z", ":regional_indicator_z:")
        await ctx.send("{text}")

def setup(client):
    client.add_cog(Ifiers(client))
