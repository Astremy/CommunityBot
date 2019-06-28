import discord

infos = {"name":"help","require":["message","commandes"],"show":3,"use":1}

async def command(message,commandes):
	await message.delete()
	if message.guild.id == 591673279828328451:
		await message.channel.send(embed=discord.Embed(title="Help",colour=discord.Colour.from_rgb(174,244,254),description="\n".join(i for i,j in commandes.items() if j[2] == 2 or j[2] == 3)),delete_after=30)
	else:
		await message.channel.send(embed=discord.Embed(title="Help",colour=discord.Colour.from_rgb(174,244,254),description="\n".join(i for i,j in commandes.items() if j[2] == 1 or j[2] == 3)),delete_after=30)