import discord
from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client
        """List of Miscellaneous Commands"""
        

    @commands.Cog.listener()
    async def on_ready(self):
         print('Polls ✅') 
    
    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        """Checks User Information"""
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(timestamp=ctx.message.created_at, title=f"User Info - {member}", color = 0xff0000)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author} | UTC Time")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, *, question):
        """Interactively creates a poll with the following question.
        To vote, use reactions!"""
        messages = [ctx.message]
        answers = []
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) <= 100
        for i in range(20):
            messages.append(await ctx.send(f'Say poll option or {ctx.prefix}cancel to publish poll.'))
            try:
                entry = await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                break
            messages.append(entry)
            if entry.clean_content.startswith(f'{ctx.prefix}cancel'):
                break
            answers.append((to_emoji(i), entry.clean_content))
        try:
            await ctx.channel.delete_messages(messages)
        except:
            pass
        answer = '\n'.join(f'{keycap}: {content}' for keycap, content in answers)
        actual_poll = await ctx.send(f'{ctx.author} asks: {question}\n\n{answer}')
        for emoji, _ in answers:
            await actual_poll.add_reaction(emoji)

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Missing the question.')

    @commands.command()
    @commands.guild_only()
    async def quickpoll(self, ctx, *questions_and_choices: str):
        """Makes a poll quickly.
        The first argument is the question and the rest are the choices."""
        if len(questions_and_choices) < 3:
            return await ctx.send('Need at least 1 question with 2 choices.')
        elif len(questions_and_choices) > 21:
            return await ctx.send('You can only have up to 20 choices.')
        perms = ctx.channel.permissions_for(ctx.me)
        if not (perms.read_message_history or perms.add_reactions):
            return await ctx.send('Need Read Message History and Add Reactions permissions.')
        question = questions_and_choices[0]
        choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]
        try:
            await ctx.message.delete()
        except:
            pass
        body = "\n".join(f"{key}: {c}" for key, c in choices)
        poll = await ctx.send(f'{ctx.author} asks: {question}\n\n{body}')
        for emoji, _ in choices:
            await poll.add_reaction(emoji)
#invite
    @commands.command()
    async def invites(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        totalInvites = 0
        for i in await ctx.guild.invites():
            if i.inviter == member:
                totalInvites += i.uses
        emby = discord.Embed(title=f"{ctx.author}", description=f"You have invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!"
, color=0xff0000)
        await ctx.send(embed=emby)

def setup(client):
    client.add_cog(Miscellaneous(client))
