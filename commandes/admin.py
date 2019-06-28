infos = {"name":"admin","require":[],"show":0,"use":0}

async def command(message,commu):
	load = open("config.json","r")
	config = json.loads(load.read())
	load.close()
	if (message.guild.id == config["server"] and str(message.channel.category_id) in commu and commu[str(message.channel.category_id)][3] == message.author.id):
		return 1
	else:
		return 0