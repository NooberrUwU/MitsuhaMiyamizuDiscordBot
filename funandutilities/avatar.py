import discord
from discord.ext import commands

class avatar(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.UserNotFound):
			embedDescription = "❌ | Please insert a valid mention!"
			embedMessage = discord.Embed(title="Error with arguments!",description=embedDescription,color=discord.Colour.from_rgb(255,182,193))
			await ctx.send(embed=embedMessage)
		else:
			print(error)

	@commands.command()
	async def avatar(self, ctx, *users : discord.User):
		if len(users) == 0:
			author = ctx.author
			avatarUrl = str(author.avatar_url_as(size=1024,static_format="png"))
			embedDescription = "Avatar Generator Machine"
			embedFooter = "Avatar of " + str(author)
			embedMessage = discord.Embed(title=embedDescription,url=avatarUrl,color=discord.Colour.from_rgb(255,182,193))
			embedMessage.set_image(url=avatarUrl)
			embedMessage.set_footer(text=embedFooter,icon_url=avatarUrl)
			await ctx.send(embed=embedMessage)
		elif len(users) == 1:
			avatarUrl = str(users[0].avatar_url_as(size=1024,static_format="png"))
			embedDescription = "Avatar Generator Machine"
			embedFooter = "Avatar of " + str(users[0])
			embedMessage = discord.Embed(title=embedDescription,url=avatarUrl,color=discord.Colour.from_rgb(255,182,193))
			embedMessage.set_image(url=avatarUrl)
			embedMessage.set_footer(text=embedFooter,icon_url=avatarUrl)
			await ctx.send(embed=embedMessage)
		else:
			embedDescription = "❌ | Invalid usage! Please use\:\n```e!avatar [USER]```"
			embedMessage = discord.Embed(title="Error with arguments!",description=embedDescription,color=discord.Colour.from_rgb(255,182,193))
			await ctx.send(embed=embedMessage)

def setup(client):
	client.add_cog(avatar(client))