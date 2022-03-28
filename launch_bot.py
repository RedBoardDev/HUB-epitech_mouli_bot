import discord
from dotenv import dotenv_values

client = discord.Client()
prefix = '$'
secrets = dotenv_values(".env")
token_discord = secrets["TOKEN_DISCORD"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith(prefix + 'oui'):
        await message.channel.send("non")

@client.event
async def on_ready():
    print('{0.user.name} is online'.format(client))

print("Connecting...")
client.run(token_discord)
