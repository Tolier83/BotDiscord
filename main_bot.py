import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="TokenDiscord.txt")


class Krobot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"{self.user.display_name} est prêt.")

    async def delete(self, number_of_messages: int):
        messages = await self.channel.history(limit=number_of_messages + 1).flatten()
        for each_message in messages:
            await each_message.delete()

    async def on_message(self, message):
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


leBot = Krobot()
leBot.run(os.getenv('TOKEN'))
