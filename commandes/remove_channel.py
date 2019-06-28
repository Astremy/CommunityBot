infos = {"name":"remove_channel","require":["message","commandes","commu"],"show":2,"use":1}

async def command(message,commandes,commu):
	if await commandes["admin"][0](message,commu):
		await message.delete()
		channs = commu[str(message.channel.category_id)][0].remove(message.channel.id)
		await message.channel.delete()