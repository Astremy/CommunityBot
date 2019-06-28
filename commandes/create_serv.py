import json

infos = {"name":"create_serv","require":[],"show":0,"use":0}

async def command(client,commu,config):
	if client.guild.id == config["server"]:
		category = await client.guild.create_category_channel(len(commu))
		chann = await category.create_text_channel("Général")
		role = await client.guild.create_role(name=str(len(commu)))
		await category.set_permissions(role,read_messages=True)
		await client.add_roles(role)
		commu[str(category.id)] = [[chann.id],[],role.id,client.id]
		load = open("commu.json","w")
		load.write(json.dumps(commu,indent=4))
		load.close()
		return category.id