import json

infos = {"name":"change_admin","require":["message","commandes","commu"],"show":2,"use":1}

async def command(message,commandes,commu):
	if await commandes["admin"][0](message,commu):
		await message.delete()
		if message.mentions:
			new = message.mentions[0]
			communaute = commu[str(message.channel.category_id)]
			if new.id in communaute[1]:
				communaute[1].remove(new.id)
				communaute[3] = new.id
				communaute[1].append(message.author.id)
				load = open("commu.json","w")
				load.write(json.dumps(commu,indent=4))
				load.close()
			else:
				await message.channel.send(content="Le joueur n'a pas été trouvé !",delete_after=15)