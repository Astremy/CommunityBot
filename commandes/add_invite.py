import json
import discord

infos = {"name":"add_invite","require":[],"show":0,"use":0}

async def command(player,channel,reponse,config):
	await channel.send(embed=discord.Embed(title="Commu",colour=discord.Colour.from_rgb(174,244,254),description=config["invite"]))
	load = open("invites.json","r")
	invites = json.loads(load.read())
	load.close()
	invites[str(player.id)] = reponse
	load = open("invites.json","w")
	load.write(json.dumps(invites,indent=4))
	load.close()