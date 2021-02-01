import discord
from discord.ext import commands

class help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx):
		embedDescription = "123"
		embedContent = discord.Embed(title="Abilities list", color=discord.Colour.from_rgb(255,182,193), description=embedDescription)
		embedContent.set_footer(text="Updated: 1/10/2021")
		await ctx.send(embed=embedContent)

def setup(client):
	client.add_cog(help(client))