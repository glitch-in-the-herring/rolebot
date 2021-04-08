import discord
from discord.ext import commands

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
		role = guild.get_role(role_id)
		await author.add_roles(role, reason="Selfbot role")

def setup(bot):
	bot.add_cog(Selfrole(bot))		