import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    """List of Fun commands!"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Fun ✅') 

#RANDOM
    @commands.command()
    async def howgay(self, ctx, member: discord.Member = None):
        """Checks howgay you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="gay r8er :rainbow_flag:" ,description=f"{member.mention} is `{percent}%` gay.", color = 0x800080)
        await ctx.send(embed=embed)
    @commands.command()
    async def iq(self, ctx, member: discord.Member = None):
        """Checks how smart you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="iq r8" ,description=f"{member.mention}'s IQ is `{percent}%`.", color = 0xffb6c1)
        await ctx.send(embed=embed)
    @commands.command()
    async def simprate(self, ctx, member: discord.Member = None):
        """Checks how simpy you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="simp r8" ,description=f"{member.mention} is `{percent}%` simp.", color = 0x8f40ff)
        await ctx.send(embed=embed)
        
#TEXT
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
        await ctx.send(f"{text}")      
#RANDOM CHOICE
    @commands.command(pass_context=True)
    async def yesno(self, ctx, *, text):
        """Answers Yes or No"""
        choice = random.randint(1, 2)
        if choice == 1:
            await ctx.send(f"{ctx.author.mention}```diff\n-Yes```")
        if choice == 2:
            await ctx.send(f"{ctx.author.mention}```diff\n-No```")

    @commands.command(pass_context=True)
    async def flipcoin(self, ctx, *, text):
        """Answers Heads or Tails"""
        choice = random.randint(1, 2)
        if choice == 1:
            await ctx.send(f"{ctx.author.mention} :coin:```fix\nHeads```")
        if choice == 2:
            await ctx.send(f"{ctx.author.mention} :coin:```fix\nTails```")

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        embed = discord.Embed(title=f"{ctx.author.mention} 8ball :8ball:")
        embed.add_field(name=f"Question: {question}", value=f"Answer: {random.choice(responses)}", inline=True)
        await ctx.send(embed=embed)
#UNICODES
    @commands.command()
    async def owo(self, ctx):
        """sends random OwO"""
        responses = [
            "OwO",
            "ÓwÒ",
            "ÒwÓ",
            "□w□",
            "●w●"
            "♡w♡",
            ">w<",
            "^w^",
            "^w^",
            "XwX",
            "・w・",
            ":eye::lips::eye:",
            "◕w◕",
            "✧w✧",
            "☆w☆",]
        await ctx.send(f"{random.choice(responses)}")
    @commands.command()
    async def lenny(self, ctx):
        """sends random lenny"""
        responses = [
            "ʕ ͡° ͜ʖ ͡°ʔ",
            "( ͡° ͜ʖ ͡°)",
            "[૦ઁ ͜つ૦ઁ]",
            "¯\_ᵔ ͜ʖᵔ_/¯",
            "( ͡° ʖ̯ ͡°)",
            "( ͡°:tongue: ͡°)",
            "( ಠ ͜ʖಠ)",
            "( ͡:eye: ͜ʖ ͡:eye:)",
            "( ͠° ͟ʖ ͡°)",
            "q⊜ᨎ⊜p",
            "(⌐■_■)"
            "ᘳ👁️‸👁️ᘰ"
            "⤜(☼Ꮂ☼)⤏",
            "(ง˵ ͡~~ ͡°˵)ง",
            "(੭◕ل͜◕)੭̸*✩⁺˚",
            "( ͡°﹏ ͡°)"
            "─=≡Σᕕ($v$)ᕗ",
            "ᑴ✧⏠✧ᑷ"]
        await ctx.send(f"{random.choice(responses)}")
    @commands.command()
    async def donger(self, ctx):
        """sends random lenny"""
        responses = [
            "ヽ༼ຈل͜ຈ༽ﾉ",
            "ヽ༼ ͠ಠل͜ ಠ ༽ﾉ",
            "ヽ༼ ಠ_ಠೃ ༽ﾉ¯",
            "♬♩♪♩ヽ༼｡> ل͜ <｡༽ﾉ♬♩♪♩)",
            "ヽ༼ ˘ل͜ ˘ ༽ﾉ",
            "ヽ༼☉ɷ⊙༽ﾉ",
            "ヽ༼≖ ɷ≖༽ﾉ",
            "ヽ༼ °◞౪◟° ༽ﾉ",
            "ヽ༼ ͠ ͡° ͜ʖ ͡° ༽ﾉ",
            "ヽ༼ ಥ_ಥ༽ﾉ",
            "ヽ༼ °ᴥ° ༽ﾉ",
            "ヽ༼ °﹃° ༽ﾉ",
            "ヽ༼ °,_｣° ༽ﾉ",
            "ヽ༼இل͜இ༽ﾉ",
            "ヽ༼ ♥ ل͜ ♥ ༽ﾉ"
            "ヽ༼ ͠° ͟ل͜ ͠° ༽ﾉ",
            "ヽ༼◉_◔ ༽ﾉ"]
        await ctx.send(f"{random.choice(responses)}")

def setup(client):
    client.add_cog(Fun(client))
