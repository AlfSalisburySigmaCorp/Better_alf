import os
import discord
import time

import quotelist as ql

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# checks the event of the user logging in using a decorator on function: event
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


# checks the event of the user sending a message using a decorator on function: event


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('//hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith("//kys"):
    await message.channel.send("Dayum nigga wtf")

  elif message.content.startswith('//who was in paris'):
    await message.channel.send('Da Niggas')

  elif message.content.startswith("//jquote") or message.content.startswith("//Jquote"):
    await message.channel.send(ql.Jacob_quote(ql.jquotes))

  elif 'kys' in message.content.lower():
    for i in range(1000):
      time.sleep(0.2)
      await message.channel.send('KILL YOURSELF!!!!!!')
    
# runs the program inside the bot with the specified token (in secrets tab)
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e
