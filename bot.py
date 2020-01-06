import os
import dbl
import discord
from discord.ext import commands
TOKEN = 'NjYzNzg5MjMwMDczNTc3NTE0.XhNqjQ.8EJu33O9E9OoIR33ERoLzpZDtFM'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
