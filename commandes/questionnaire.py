import json
import discord

infos = {"name":"questionnaire","require":[],"show":0,"use":0}
#truc = {message.id:[state,rep]}
questions = [["Quelle est votre principale passion ?",["Gaming","Musique","Sport","Lecture"],["🎮","🎧","⚽","📘"]],["Quel est votre age ?",["- de 13 ans","13 - 16 ans","16 - 18 ans","18 - 21 ans","+ de 21 ans"],["{}\N{COMBINING ENCLOSING KEYCAP}".format(num) for num in range(0, 5)]]]

async def command(reaction,questionnaire,user,commandes,config,value=1,channel=None):
	if value:
		message = reaction.message
		donnees = questionnaire[str(message.id)]
		print(questions[donnees[0]][2])
		print(reaction.emoji)
		if not reaction.emoji in questions[donnees[0]][2]:
			return
		donnees[1] += str(questions[donnees[0]][2].index(reaction.emoji))
		print(donnees[1])
		channel = message.channel
	else:
		donnees = [-1,""]
		message = reaction
	donnees[0] += 1
	if len(questions) == donnees[0]:
		del(questionnaire[str(message.id)])
		return await commandes["add_invite"][0](user,channel,donnees[1],config)
	new = await channel.send(embed=discord.Embed(title=questions[donnees[0]][0],colour=discord.Colour.from_rgb(174,244,254),description="\n".join(questions[donnees[0]][2][i] + " : " + questions[donnees[0]][1][i] for i in range(len(questions[donnees[0]][1])))))
	for i in range(len(questions[donnees[0]][1])):
		await new.add_reaction(questions[donnees[0]][2][i])
	questionnaire[str(new.id)] = donnees
	if value:
		del(questionnaire[str(message.id)])
	load = open("questionnaire.json","w")
	load.write(json.dumps(questionnaire,indent=4))
	load.close()