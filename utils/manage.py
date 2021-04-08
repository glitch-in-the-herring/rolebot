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
