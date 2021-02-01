import discord
import random
import json
from discord.ext import commands

class generatekey(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def generatekey(self, ctx):	
		var_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		key = ""
		for x in range(20):
			random_number = random.randint(0,61)
			character = var_string[random_number]
			key += character
		await ctx.send("**Your new key is**: " + key)
		authorId = ctx.author.id
		with open("data/key.json","r") as data:
			storedData = json.load(data)
		storedData[authorId] = key
		with open("data/key.json","w") as data:
			json.dump(storedData, data, indent=4)

def setup(client):
	client.add_cog(generatekey(client))