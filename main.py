import discord
from discord.ext import commands
import asyncio
import random
import os

botid = "585401301731377163"

client = discord.Client()
a = "610063326872993823"
b = "610063375082192926"
               
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
  global a
  global b
  mess = message.content.lower()
  auth = message.author.id
  channel = message.channel
  #if auth == botid:
    a = b
    b = message
    
  if mess == "ar?":
      await a.add_reaction('⬅')
      await a.add_reaction('➡')
        
 
client.run(os.environ['BOT_TOKEN'])
