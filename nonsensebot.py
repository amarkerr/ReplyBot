#Simple nonsense bot

import os
import discord
from replit import db

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

token = os.environ['TOKEN']
img_path = 'reset-the-clock-pacific-rim.gif'
clock_words = ['update']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/reset'):
        with open(img_path, 'rb') as gif:
          await message.channel.send(file=discord.File(gif, 'reset-the-clock-pacific-rim.gif'))
      
    if any (word in message.content for word in clock_words):
      with open(img_path, 'rb') as gif:
        await message.channel.send(file=discord.File(gif, 'reset-the-clock-pacific-rim.gif'))

client.run(token)
