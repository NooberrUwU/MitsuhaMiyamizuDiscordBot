import discord
import json
from discord.ext import commands

class rulesaccept(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def rulesaccept(self, ctx):
		authorId = ctx.author.id
		try:
			with open("data/rules.json","r") as data:
				stored_data = json.load(data)
			accept_status = stored_data[str(authorId)]["accept_status"]
			if accept_status == True:
				await ctx.send("🤔 Uh oh!! You have already accepted our rules :\) Feel free to use the bot!")
				stored_data[str(authorId)]["accept_message_id"] = None
				with open("data/rules.json","w") as data:
					json.dump(stored_data,data,indent=4)
			elif accept_status == False:
				await ctx.send("✅ You have accepted our rules!")
				stored_data[str(authorId)]["accept_message_id"] = None
				stored_data[str(authorId)]["accept_status"] == True
				with open("data/rules.json","w") as data:
					json.dump(stored_data,data,indent=4)
		except:
			await ctx.send("✅ You have accepted our rules!")
			with open("data/rules.json","r") as data:
				stored_data = json.load(data)
			stored_data[str(authorId)] = {}
			stored_data[str(authorId)]["accept_message_id"] = None
			stored_data[str(authorId)]["accept_status"] = True
			with open("data/rules.json","w") as data:
				json.dump(stored_data,data,indent=4)
def setup(client):
	client.add_cog(rulesaccept(client))