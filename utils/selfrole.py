import discord
from discord.ext import commands
import utils.db as db

class Selfrole(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="giverole",
	)
	async def giverole(self, ctx, alias):
		guild = ctx.guild
		author = ctx.author
		role_id = db.search_role(alias)
		print(role_id)
		role = guild.get_role(role_id)
		await author.add_roles(role, reason="Selfbot role")
		await ctx.send("role given")

def setup(bot):
	bot.add_cog(Selfrole(bot))		