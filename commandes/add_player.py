import json

infos = {"name":"add_player","require":[],"show":0,"use":0}

async def command(client,commu,serv):
	if not client.id in commu[str(serv)][1]:
		commu[str(serv)][1].append(client.id)
		role = commu[str(serv)][2]
		role = client.guild.get_role(role)
		await client.add_roles(role)
		load = open("commu.json","w")
		load.write(json.dumps(commu,indent=4))
		load.close()