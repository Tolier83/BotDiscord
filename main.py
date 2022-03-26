import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="TokenDiscord.txt")

default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt.")


@client.event
async def on_member_join(member):
    print(member.display_name + " est arriver sur le serveur")
    general_channel: discord.TextChannel = client.get_channel(956501889824989235)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")


@client.event
async def on_member_remove(member):
    print(member.display_name + " est partie")
    general_channel: discord.TextChannel = client.get_channel(956501889824989235)
    await general_channel.send(content=f"Adieux {member.display_name} !")


@client.event
async def on_message(message):
    print("message :" + message.content + " where :" + message.channel.name + " who :" + message.author.name)
    if message.content.lower() == "ping":
        await message.channel.send("pong, ahah marrant ça " + message.author.name)
    if message.content.lower() == "keskisepasse?":
        await message.channel.send(
            "message :" + message.content + " where :" + message.channel.name + " who :" + message.author.name)
    if message.content.startswith("!role"):
        what = (message.content.split()[1])
        who = (message.content.split()[2])
        role = (message.content.split()[3])
        print("what :" + what + " who: " + who + "name: " + role)
        print(who.permission)
        # await who.edit("role")


client.run(os.getenv('TOKEN'))
