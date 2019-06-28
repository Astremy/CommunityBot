infos = {"name":"rename_channel","require":["message","commandes","commu","args"],"show":2,"use":1}

async def command(message,commandes,commu,args):
	if await commandes["admin"][0](message,commu):
		await message.delete()
		channs = commu[str(message.channel.category_id)][0]
		for i in channs:
			if i == message.channel.id:
				await message.channel.edit(name=" ".join(args))