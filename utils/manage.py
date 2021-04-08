import discord
from discord.ext import commands
import utils.db as db

class Manage(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="addrole",
	)
	async def addrole(self, ctx, role:discord.Role, category:str="", alias:str=""):
		if len(alias) != 0:
			for aliases in alias.split("|"):
				db.add_role_alias(role.id, alias)
		if len(category) != 0:
			db.add_role_category(role.id, category)
		db.commit()

def setup(bot):
	bot.add_cog(Manage(bot))			