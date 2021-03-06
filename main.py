import argparse
import json
import logging
import os
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO,
		format='%(asctime)s %(levelname)-8s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S'
	)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", 
	metavar='TOKEN', 
	help="Bot token. Keep this secret"
)
parser.add_argument("-p", "--prefix", 
	metavar='PREFIX', 
	default="^", 
	help="Bot prefix. Used to invoke the bot commands. Defaults to ^"
)
parser.add_argument("-s", "--sysadmin", 
	metavar='ID', 
	help="Sysadmin user ID"
)
args = parser.parse_args()
token, prefix, sysadmin_id = args.token, args.prefix, args.sysadmin

try:
	with open("config.json", "r+") as f:
		config = json.load(f)
		if not token:
			token = config["token"]
		if not prefix:
			prefix = config["prefix"]		
		if not sysadmin_id:
			sysadmin_id = config["sysadmin_id"]
except IOError:
	with open("config.json", "w") as f:
		print("Welcome to the setup for Rolebot!")
		config = {}

		if not token:
			token = input("Please enter your bot's token: ")
			config["token"] = token
		else:
			config["token"] = token			
		if not sysadmin_id:
			sysadmin_id = input("Please enter your user ID, or the sysadmin's ID: ")
			config["sysadmin_id"] = sysadmin_id
		else:
			config["sysadmin_id"] = sysadmin_id

		json.dump(config, f)

		print("All done!")

intents = discord.Intents(
	messages=True, 
	guilds=True, 
	members=True,
	reactions=True,
)

bot = commands.Bot(command_prefix=prefix, intents=intents)

bot.load_extension("utils.manage")
bot.load_extension("utils.selfrole")

bot.run(token)