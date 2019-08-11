import discord
from discord.ext import commands
import asyncio
import random
import os

client = discord.Client()
a = 0
b = 0
               
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
  global a
  global b
  a = b
  b = message
  mess = message.content.lower()
  auth = message.author
  channel = message.channel
  if mess == "arrows?":
      await a.add_reaction('⬅️')
      await a.add_reaction('➡️')
        
 
client.run(os.environ['BOT_TOKEN'])
