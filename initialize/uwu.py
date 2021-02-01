import discord
import random
from discord.ext import commands

class uwu(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		activityNamelist = ["Tenki no Ko","Kimi no Nawa","Boku no Pico","5 Centimeters Per Second"]
		await self.client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=f"the \"{random.choice(activityNamelist)}\"",type=discord.ActivityType.watching))
		print("Bot is ready!")

	# @commands.Cog.listener()
	# async def on_ready(self):
	# 	await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,name="HKISO with the boiz!"))
	# 	print("Bot is ready!")

def setup(client):
	client.add_cog(uwu(client))