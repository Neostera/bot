import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    """List of Fun commands!"""
    @commands.Cog.listener()
    async def on_ready(self):
         print('Fun ✅') 

#RANDOM
    @commands.command(aliases=['gayness', 'gayrate', 'gayr8'])
    async def howgay(self, ctx, member: discord.Member = None):
        """Checks howgay you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="gay r8er :rainbow_flag:" ,description=f"{member.mention} is `{percent}%` gay.", color = 0x800080)
        await ctx.send(embed=embed)
    @commands.command(aliases=['howsmart', 'smartness', 'brain', 'smartrate'])
    async def iq(self, ctx, member: discord.Member = None):
        """Checks how smart you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="iq r8" ,description=f"{member.mention}'s IQ is `{percent}%`.", color = 0xffb6c1)
        await ctx.send(embed=embed)
    @commands.command(aliases=['simpness', 'howsimp'])
    async def simprate(self, ctx, member: discord.Member = None):
        """Checks how simpy you are"""
        if not member:  # if member is no mentioned
           member = ctx.message.author
        percent = random.randint(0, 101)
        embed = discord.Embed(title="simp r8" ,description=f"{member.mention} is `{percent}%` simp.", color = 0x8f40ff)
        await ctx.send(embed=embed)
        
#TEXT

#RANDOM CHOICE
    @commands.command(pass_context=True, aliases=['noyes'])
    async def yesno(self, ctx, *, text):
        """Answers Yes or No"""
        choice = random.randint(1, 2)
        if choice == 1:
            await ctx.send(f"{ctx.author.mention}```diff\n-Yes```")
        if choice == 2:
            await ctx.send(f"{ctx.author.mention}```diff\n-No```")

    @commands.command(pass_context=True, aliases=['tailsheads', 'headsortails', 'flipcoin'])
    async def coinflip(self, ctx, *, text):
        """Answers Heads or Tails"""
        choice = random.randint(1, 2)
        if choice == 1:
            await ctx.send(f"{ctx.author.mention} :coin:```fix\nHeads```")
        if choice == 2:
            await ctx.send(f"{ctx.author.mention} :coin:```fix\nTails```")

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        embed = discord.Embed(title=f"{ctx.author} 8ball :8ball:")
        embed.add_field(name=f"Question: {question}", value=f"Answer: {random.choice(responses)}", inline=True)
        await ctx.send(embed=embed)
#UNICODES
    @commands.command()
    async def owo(self, ctx):
        """sends random OwO"""
        responses = [
            "OwO", "ÓwÒ", "ÒwÓ", "□w□", "●w●", "♡w♡", ">w<", "^w^", "^w^", "XwX", "・w・", ":eye::lips::eye:", "◕w◕", "✧w✧", "☆w☆"]
        await ctx.send(f"{random.choice(responses)}")
    @commands.command()
    async def lenny(self, ctx):
        """sends random lenny"""
        responses = [
            "ʕ ͡° ͜ʖ ͡°ʔ", "( ͡° ͜ʖ ͡°)", "[૦ઁ ͜つ૦ઁ]", "¯\_ᵔ ͜ʖᵔ_/¯", "( ͡° ʖ̯ ͡°)", "( ͡°:tongue: ͡°)", "( ಠ ͜ʖಠ)", "( ͡:eye: ͜ʖ ͡:eye:)", "( ͠° ͟ʖ ͡°)", "q⊜ᨎ⊜p", "(⌐■_■)", "ᘳ👁️‸👁️ᘰ", "⤜(☼Ꮂ☼)⤏", "(ง˵ ͡~~ ͡°˵)ง", "(੭◕ل͜◕)੭̸*✩⁺˚", "( ͡°﹏ ͡°)", "─=≡Σᕕ($v$)ᕗ", "ᑴ✧⏠✧ᑷ"]
        await ctx.send(f"{random.choice(responses)}")
    @commands.command()
    async def donger(self, ctx):
        """sends random lenny"""
        responses = [
            "ヽ༼ຈل͜ຈ༽ﾉ", "ヽ༼ ͠ಠل͜ ಠ ༽ﾉ", "ヽ༼ ಠ_ಠೃ ༽ﾉ¯", "♬♩♪♩ヽ༼｡> ل͜ <｡༽ﾉ♬♩♪♩)", "ヽ༼ ˘ل͜ ˘ ༽ﾉ", "ヽ༼☉ɷ⊙༽ﾉ", "ヽ༼≖ ɷ≖༽ﾉ", "ヽ༼ °◞౪◟° ༽ﾉ", "ヽ༼ ͠ ͡° ͜ʖ ͡° ༽ﾉ", "ヽ༼ ಥ_ಥ༽ﾉ", "ヽ༼ °ᴥ° ༽ﾉ", "ヽ༼ °﹃° ༽ﾉ", "ヽ༼ °,_｣° ༽ﾉ", "ヽ༼இل͜இ༽ﾉ", "ヽ༼ ♥ ل͜ ♥ ༽ﾉ", "ヽ༼ ͠° ͟ل͜ ͠° ༽ﾉ", "ヽ༼◉_◔ ༽ﾉ"]
        await ctx.send(f"{random.choice(responses)}")

def setup(client):
    client.add_cog(Fun(client))
