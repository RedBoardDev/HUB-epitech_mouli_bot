
import asyncio
from discord.ext import commands

prefix = '$'

class manageMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.event
    async def on_message(message):
        if message.author == client.user:
            return
        msg = message.content
        if msg.startswith(prefix + 'oui'):
            await message.channel.send("non")


def setup(client):
    client.add_cog(manageMessage(client))