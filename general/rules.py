import time
import json
import discord
from discord.ext import commands

class rules(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def rules(self, ctx, *args):
		embedMessageDecription1 = "**RULES AND REGULATIONS AGREEMENT:**\n\n*\*Failure to follow these rules will result in a ban and/or account reset. You also have to obey the [**Discord Community Guidelines**](https://discord.com/guidelines).*\n\n• Any actions performed to gain an unfair advantage over other users are explicitly against the rules.\nThis includes but not limited to:\n├> Using macros/scripts for any commands\n└> Using multiple accounts for any reason\n\n• Do not use any exploits and report any found in the bot.\n\n• You can not sell/trade coin or any bot goods for anything outside of the bot.\n*\*This is called as In Real Life Trading (IRL Trading) by real money!*\n\n• If you have any questions come ask us in our server!\n*\*Our support server is in developing status. Sorry for the inconvenience!*\n\nThese rules are based on **OwO Discord Bot Rules**.\nPlease react to this emoji ✅ within 20 seconds to accept these rules before using the bot! An another way to accept these rules is typing: ```e!rulesaccept```"
		embedMessage1 = discord.Embed(title="Mitsuha Miyamizu Discord Bot - Terms & Conditions",url="https://discord.com/guidelines",description=embedMessageDecription1, color=discord.Colour.from_rgb(255,182,193))
		message = await ctx.send(embed=embedMessage1)
		await message.add_reaction("✅")
		messageId = message.id
		authorId = ctx.author.id

		try:
			with open("data/rules.json","r") as data:
				stored_data = json.load(data)
			stored_data[str(authorId)]["accept_message_id"] = messageId
			if stored_data[str(authorId)]["accept_status"] == True:
				pass
			elif stored_data[str(authorId)]["accept_status"] == False:
				stored_data[str(authorId)]["accept_status"] = False
			with open("data/rules.json","w") as data:
				json.dump(stored_data,data,indent=4)
		except:
			with open("data/rules.json","r") as data:
				stored_data = json.load(data)
			stored_data[str(authorId)] = {}
			stored_data[str(authorId)]["accept_message_id"] = messageId
			stored_data[str(authorId)]["accept_status"] = False
			with open("data/rules.json","w") as data:
				json.dump(stored_data,data,indent=4)
def setup(client):
	client.add_cog(rules(client))