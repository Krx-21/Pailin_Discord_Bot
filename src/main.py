# main.py
# This is the main file to run the Pailin Discord Bot.

import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True # Enable message content intent for reading messages

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('Pailin is ready to go!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')

if __name__ == "__main__":
    if not DISCORD_BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN not found in .env file.")
    else:
        bot.run(DISCORD_BOT_TOKEN)
