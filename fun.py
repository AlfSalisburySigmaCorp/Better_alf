@client.event
async def on_message(message):
    if 'kys' in message.content.lower():
        await message.channel.send('KILL YOURSELF!!!!!!')