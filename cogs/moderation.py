import discord
from discord.ext import commands
import datetime
from database import cursor, conn

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason"):
        cursor.execute(
            "INSERT INTO infractions (user_id, reason, moderator, time) VALUES (?, ?, ?, ?)",
            (member.id, reason, ctx.author.name, str(datetime.datetime.now()))
        )
        conn.commit()
        await ctx.send(f"⚠️ Warned {member.mention}: {reason}")

def setup(bot):
    bot.add_cog(Moderation(bot))
