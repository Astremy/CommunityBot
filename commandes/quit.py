infos = {"name":"quit","require":["message","client"],"show":0,"use":1}

async def command(message,client):
	if message.author.id == 263331548542009348:
		await message.delete()
		await client.logout()