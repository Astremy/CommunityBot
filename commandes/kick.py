import json

infos = {"name":"kick","require":["message","commandes","commu"],"show":2,"use":1}

async def command(message,commandes,commu):
	if await commandes["admin"][0](message,commu):
		await message.delete()
		if message.mentions:
			perso = message.mentions[0]
			if perso:
				commu[str(message.channel.category_id)][1].remove(perso.id)
				role = commu[str(message.channel.category_id)][2]
				role = message.guild.get_role(role)
				await perso.remove_roles(role)
				load = open("commu.json","w")
				load.write(json.dumps(commu,indent=4))
				load.close()
			else:
				await message.channel.send(content="Le joueur n'est pas sur le serveur",delete_after=15)