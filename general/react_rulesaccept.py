import discord
import json
from discord.ext import commands

class react_rulesaccept(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, user):
		messageId = reaction.message.id
		userId = user.id
		channel = reaction.message.channel
		if userId != 790180126565335111:
			try:
				with open("data/rules.json","r") as data:
					stored_data = json.load(data)
				accept_status = stored_data[str(userId)]["accept_status"]
				accept_messageId = stored_data[str(userId)]["accept_message_id"]
				if messageId == accept_messageId:
					if accept_status == False:
						await channel.send("✅ You have accepted our rules!")
						stored_data[str(userId)]["accept_status"] = True
						stored_data[str(userId)]["accept_message_id"] = None
						with open("data/rules.json","w") as data:
							json.dump(stored_data,data,indent=4)
					elif accept_status == True:
						await channel.send("🤔 Uh oh!! You have already accepted our rules :\) Feel free to use the bot!")
						stored_data[str(userId)]["accept_message_id"] = None
						with open("data/rules.json","w") as data:
							json.dump(stored_data,data,indent=4)
					else:
						pass
				else:
					pass
			except:
				pass
		else:
			pass

def setup(client):
	client.add_cog(react_rulesaccept(client))