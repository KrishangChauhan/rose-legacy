import discord
from discord.ext import commands
from database import get_user, cursor, conn

class Legacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        user = get_user(member.id)

        embed = discord.Embed(title=f"🌹 {member.name}'s Profile", color=0xff0055)
        embed.add_field(name="Roses", value=user[1])
        embed.add_field(name="Kills", value=user[2])
        embed.add_field(name="Deaths", value=user[3])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveroses(self, ctx, member: discord.Member, amount: int):
        get_user(member.id)
        cursor.execute("UPDATE users SET roses = roses + ? WHERE user_id = ?", (amount, member.id))
        conn.commit()
        await ctx.send(f"🌹 Gave {amount} roses to {member.mention}")

def setup(bot):
    bot.add_cog(Legacy(bot))
