import json

infos = {"name":"start_quest","require":["questionnaire","message","commandes","config"],"show":1,"use":1}

async def command(questionnaire,message,commandes,config):
	await message.delete()
	if message.author.dm_channel == None:
		await message.author.create_dm()
	chann = message.author.dm_channel
	return await commandes["questionnaire"][0](reaction=message,questionnaire=questionnaire,config=config,value=0,channel=chann,commandes=commandes,user=message.author)