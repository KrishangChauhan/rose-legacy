import discord
from discord.ext import commands
from database import get_user, cursor, conn

class PvP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addkill(self, ctx, killer: discord.Member, victim: discord.Member):
        get_user(killer.id)
        get_user(victim.id)

        cursor.execute("UPDATE users SET kills = kills + 1 WHERE user_id = ?", (killer.id,))
        cursor.execute("UPDATE users SET deaths = deaths + 1 WHERE user_id = ?", (victim.id,))
        conn.commit()

        await ctx.send(f"⚔️ {killer.mention} killed {victim.mention}")

def setup(bot):
    bot.add_cog(PvP(bot))
