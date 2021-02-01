import discord
import sys
import os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
PREFIX = "e!"

# sys.dont_write_bytecode = True

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')

for filename in os.listdir("./general"):
	if filename.endswith(".py"):
		client.load_extension(f"general.{filename[:-3]}")

for filename in os.listdir("./funandutilities"):
	if filename.endswith(".py"):
		client.load_extension(f"funandutilities.{filename[:-3]}")

for filename in os.listdir("./initialize"):
	if filename.endswith(".py"):
		client.load_extension(f"initialize.{filename[:-3]}")

for filename in os.listdir("./economy"):
	if filename.endswith(".py"):
		client.load_extension(f"economy.{filename[:-3]}")

for filename in os.listdir("./zoom"):
	if filename.endswith(".py"):
		client.load_extension(f"zoom.{filename[:-3]}")

client.run(TOKEN)