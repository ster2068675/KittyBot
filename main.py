import discord
import os
#allows code to make https requests to retrieve data from api
import aiohttp
import asyncio
#api returns JSON
import json
import random
from replit import db
# param dict to query_string
from urllib.parse import urlencode 

client = discord.Client()

init_triggers = ["treat", "eat", "snack", "toy", "scratch", "scritch", "fish", "fishing", "food", "itchy", "cat", "kitty", "meat"]

if "ready" not in db.keys():
  db["ready"] = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  msg = message.content

  if msg.startswith('!hello'):
    await message.channel.send('Meow!')

  if any(word in msg for word in init_triggers):
    await message.channel.send('Meooow!')

    if msg.startswith('!kitty'):
      await message.channel.send('almost ready!')
      await randomKitty(message)
      print("funct executed")
      

    #specific breed : !kitty siamese 

#"msg recvd"
async def randomKitty(message):
  await getImage(message.author.username)
  print("working so far")

async def getImage(msg_id):
  headers = {'x-api-key': 'cat_key'}

  params = {
    'has_breed': True,
    'mime_types': 'jpg, png',
    'size': 'small',
    'limit': 1 
    }

  query_string = urlencode(params)

  try:
    url = '{}v1/images/search?{}'.format('cat_api', query_string)
    async with aiohttp.ClientSession() as session:
          async with session.get(url, headers) as response:
            html = await response.text()
            json_data = json.loads(html)
  except:
    print("uh oh... something wrong w the url?")
  else:
    print("successful get!")
    return json_data



#dont give away tokens to strangers lol
client.run(os.environ['TOKEN'])