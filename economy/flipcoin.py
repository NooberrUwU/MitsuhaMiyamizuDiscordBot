import discord
import json
import random
from discord.ext import commands

class flipcoin(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def flipcoin(self, ctx, *args):
		if len(args) == 0:
			random_number = random.randint(1,2)
			if random_number == 1:
				await ctx.send("💰 **Economy** | You got a tail!")
			elif random_number == 2:
				await ctx.send("💰 **Economy** | You got a head!")
			else:
				await ctx.send("💰 **Economy** | An error has occurred while running the command!... This error will be automatically reported to the staffs!")
		elif len(args) == 2:
			authorId = ctx.author.id
			try:
				if int(args[0]) < 1:
					await ctx.send("💰 **Economy** | Please input a valid number of coin! (3)")
				elif int(args[0]) >= 1:
					try:
						with open("data/economy.json","r") as data:
							storedData = json.load(data)
						coins = storedData[str(authorId)]["wallet"]
						random_number = random.randint(1,2)
						if args[1].lower() == "head":
							selected_number = 1
							if random_number == selected_number:
								await ctx.send("💰 **Economy** | **Congratulations!** Your wallet has been added **" + str(coins) + "** coins!")
							elif random_number != selected_number:
								await ctx.send("💰 **Economy** | **Yikes!** Your wallet has lost **" + str(coins) + "** coins!")

						elif args[1].lower() == "tail":
							selected_number = 2
							if random_number == selected_number:
								await ctx.send("💰 **Economy** | **Congratulations!** Your wallet has been added **" + str(coins) + "** coins!")
							elif random_number != selected_number:
								await ctx.send("💰 **Economy** | **Yikes!** Your wallet has lost **" + str(coins) + "** coins!")
						else:
							await ctx.send("💰 **Economy** | Please input **HEAD** or **TAIL**! (2)")
					except Exception as e:
						await ctx.send("💰 **Economy** | You haven't set your bank account yet! Create one by typing this: ```e!wallet```")
				else:
					await ctx.send("💰 **Economy** | An error has occurred while running the command!... This error will be automatically reported to the staffs!")
			except:
				await ctx.send("💰 **Economy** | Please input a valid number of coin! (1)")
		else:
			pass

def setup(client):
	client.add_cog(flipcoin(client))