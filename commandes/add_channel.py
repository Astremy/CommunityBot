import json

infos = {"name":"add_channel","require":["message","commandes","commu","args"],"show":2,"use":1}

async def command(message,commandes,commu,args):
	if await commandes["admin"][0](message,commu):
		await message.delete()
		if len(commu[str(message.channel.category_id)][0]) == 5:
			return await message.channel.send(content="Il y a déjà trop de channels !",delete_after=20)
		chann = await message.guild.get_channel(message.channel.category_id).create_text_channel(" ".join(args))
		commu[str(message.channel.category_id)][0].append(chann.id)
		load = open("commu.json","w")
		load.write(json.dumps(commu,indent=4))
		load.close()