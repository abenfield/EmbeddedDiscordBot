import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

@client.event
async def on_message(message):
    if message.content.startswith("https://www.instagram.com/reel/"):
        link = message.content
        print(link)
        new_link = link.replace("instagram", "ddinstagram")
        await message.channel.send(new_link)
        await message.delete()
    elif message.content.startswith("https://www.tiktok.com/"):
        link = message.content
        new_link = link.replace("tiktok", "vxtiktok")
        await message.channel.send(new_link)
        await message.delete()
    elif message.content.startswith("https://www.facebook.com/reel/"):
        link = message.content
        new_link = "https://www.ddinstagram.com/reel/" + link.split("/reel/")[1].split("?")[0]
        await message.channel.send(new_link)
        await message.delete()
client.run(DISCORD_BOT_TOKEN)
