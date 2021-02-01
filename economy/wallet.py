import discord
import json
from discord.ext import commands

class wallet(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def wallet(self, ctx):
		authorId = ctx.author.id
		try:
			with open("data/economy.json","r") as data:
				storedData = json.load(data)
			coins = storedData[str(authorId)]["wallet"]
			await ctx.send("💰 **Economy** | Your wallet currently has **" + str(coins) + "** coins!")
		except:
			await ctx.send("💰 **Economy** | **Congratulations!** You have set up your bank account! Now you have **0** coin in your wallet.")			
			with open("data/economy.json","r") as data:
				storedData = json.load(data)
			storedData[str(authorId)] = {}
			storedData[str(authorId)]["wallet"] = 0
			with open("data/economy.json","w") as data:
				json.dump(storedData, data, indent = 4)

def setup(client):
	client.add_cog(wallet(client))