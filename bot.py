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
        new_link = link.replace("instagram", "ddinstagram")
    elif message.content.startswith("https://www.tiktok.com/"):
        link = message.content
        new_link = link.replace("tiktok", "vxtiktok")
    elif message.content.startswith("https://www.facebook.com/reel/"):
        link = message.content
        new_link = "https://www.ddinstagram.com/reel/" + link.split("/reel/")[1].split("?")[0]
    elif message.content.startswith("https://twitter.com"):
        link = message.content
        new_link = link.replace("twitter", "fxtwitter")
    elif message.content.startswith("https://x.com"):
        link = message.content
        new_link = link.replace("x", "fixupx")
    elif message.content.startswith("https://reddit.com") or message.content.startswith("https://www.reddit.com"):
        link = message.content
        new_link = link.replace("reddit", "rxddit")
    elif message.content.startswith("https://old.reddit.com"):
        link = message.content
        new_link = link.replace("old.reddit", "rxddit")
    else:
        return
    await message.channel.send(f"{message.author.display_name} posted: {new_link}")
    await message.delete()

client.run(DISCORD_BOT_TOKEN)
