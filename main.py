import discord
import json
import os
import importlib

client = discord.Client()

commandes = {}
files = os.listdir(os.path.join("commandes"))
for i in files:
	if i == "__init__.py": continue
	if i[-3:] == ".py":
		name = i[:-3]
		commande = importlib.import_module("commandes." + name)
		infos = commande.infos
		commandes[infos["name"]] = [commande.command,infos["require"],infos["show"],infos["use"]]

load = open("config.json","r")
config = json.loads(load.read())
load.close()

load = open("commu.json","r")
commu = json.loads(load.read())
load.close()

load = open("questionnaire.json","r")
questionnaire = json.loads(load.read())
load.close()

load = open("choix.json","r")
choix = json.loads(load.read())
load.close()

@client.event
async def on_ready():
	print("Bot connecté !")
	await client.change_presence(activity=discord.Game(name="!help"))

@client.event
async def on_message(message):
	if message.author.bot:
		return
	args = message.content.lower().split(" ")
	pref = config["prefix"]

	if not (len(args[0]) > len(pref) and pref == args[0][:len(pref)]): return
	else:
		comm = args.pop(0)[len(pref):]
		if comm in commandes:
			if commandes[comm][3]:
				possible = {"client":client,"message":message,"commandes":commandes,"commu":commu,"args":args,"questionnaire":questionnaire,"config":config}
				arguments = []
				for truc in commandes[comm][1]:
					try: arguments.append(possible[truc])
					except: continue
				await commandes[comm][0](*arguments)

@client.event
async def on_reaction_add(reaction,user):
	if user.bot:
		return
	print(reaction)
	if reaction.message.channel._type == 1:
		message = reaction.message
		if str(message.id) in questionnaire:
			await commandes["questionnaire"][0](reaction,questionnaire,user,commandes,config)

@client.event
async def on_member_join(member):
	if member.guild.id == config["server"]:
		load = open("invites.json","r")
		invites = json.loads(load.read())
		load.close()
		if str(member.id) in invites:
			if invites[str(member.id)] in choix:
				for serv in choix[str(invites[str(member.id)])]:
					if len(commu[str(serv)][1]) < 16:
						return await commandes["add_player"][0](member,commu,serv)
				name = await commandes["create_serv"][0](member,commu,config)
				choix[invites[str(member.id)]].append(name)
			else:
				name = await commandes["create_serv"][0](member,commu)
				choix[str(invites[str(member.id)])] = [name]
			load = open("choix.json","w")
			load.write(json.dumps(choix,indent=4))
			load.close()
		else:
			await member.guild.kick(member)

client.run(config["token"])
