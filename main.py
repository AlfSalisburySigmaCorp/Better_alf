import discord
import os
import time

import quotelist as ql
import fun as f

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
    await ql.Jacob_quote(ql.jquotes, message)

  elif 'kys' in message.content.lower():
    f.kys(message)

  elif message.content.startswith("//phones"):
    await f.phones(message)

  elif message.content.startswith("//react"):
    await f.react(f.reactions, message)

  elif message.content.startswith("//kettle"):
    await message.channel.send("https://cdn.discordapp.com/attachments/927612770709561406/1169999748200144946/Screenshot_2023-11-03-13-59-37-641_com.snapchat.android.png?ex=6557722d&is=6544fd2d&hm=91f47bfd047a535063c9bcba2871265037b957ad8fb878682a986abb1eea8399&")


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
