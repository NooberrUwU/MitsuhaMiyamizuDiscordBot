import discord
from discord.ext import commands

class templete(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener()
	async def on_ready(self):
		print("Cogs templetes are working very well!")

	@commands.command()
	async def ping(self, ctx):
		await ctx.send("Pong!")
		await ctx.send("<:uwu:737166566638092299>")

def setup(client):
	client.add_cog(templete(client))