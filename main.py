import os
import discord

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

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


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
