import discord
import time
from discord.ext import commands

class zoomid(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def zoomid(self, ctx, *args):
		# embedDescription = "A year ago, we introduced to you guys the **Zoom Meeting IDs Display Command**. And now, with the blow up of COVID-19, we opened this command again with more updates and fixed issues!\n\nThis command is always in the heavy development status. **These IDs can be changed in anytime**. If you have any question, just DM me!\n\nBy the way, the embed content will be deleted after **30 seconds**, count up since you execute the command."
		# embedContent = discord.Embed(title="List of Meeting IDs of 9A2 Teachers",description=embedDescription,color=discord.Colour.from_rgb(255,182,193))
		# message1 = await ctx.send(embed=embedContent)

		# embedContent2 = discord.Embed(color=discord.Colour.from_rgb(255,182,193))
		# embedContent2.add_field(name="Subjects‏‏‎", value="1) Maths\n2) Literature\n3) English\n4) History\n5) Civic Education\n6) Geography\n7) Biology\n8) Chemistry\n9) Physics\n10) Technology\n11) Music\n12) Physical Education\n13) Arts\n14) Informatics Technology (IT)", inline=True)
		# embedContent2.add_field(name="Meeting IDs‏‏‎", value="3345081082\n5320894930\n6472181785\n3894189011\n8102536065\n4636921326\n9837833699\n6253175884\n6570777853\n2686024835\n71887586251\nCurrently unknown\nCurrently unknown\nCurrently unknown", inline=True)
		# embedContent2.add_field(name="Passcode‏‏‎s", value="1234567\n825648\n123456\n906409\n493755\n123\n9999\n888888\n4546\n766848\n210055\nCurrently unknown\nCurrently unknown\nCurrently unknown", inline=True)
		# message2 = await ctx.send(embed=embedContent2)

		embedContent2 = discord.Embed(color=discord.Colour.from_rgb(255,182,193))
		embedContent2.add_field(name="Môn học", value="1) Toán\n2) Ngữ văn\n3) Tiếng Anh\n4) Lịch sử\n5) GDCD\n6) Địa lý\n7) Sinh học\n8) Hóa học\n9) Vật lý\n10) Công nghệ\n11) Âm nhạc\n12) Thể dục\n13) Mỹ thuật\n14) Tin học", inline=True)
		embedContent2.add_field(name="Meeting IDs‏‏‎", value="3345081082\n5320894930\n6472181785\n3894189011\n8102536065\n4636921326\n9837833699\n6253175884\n6570777853\n2686024835\n71887586251\n~\n~\n~", inline=True)
		embedContent2.add_field(name="Passcode‏‏‎s", value="1234567\n825648\n123456\n906409\n493755\n123\n9999\n888888\n004546\n766848\n210055\n~\n~\n~", inline=True)
		message2 = await ctx.send(embed=embedContent2)

		time.sleep(30)
		# await message1.delete()
		messageX = ctx.m
		await messageX.delete()
		await message2.delete()

def setup(client):
	client.add_cog(zoomid(client))
