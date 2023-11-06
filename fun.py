import time
import random as r


def phones(message):
  return message.channel.send("i got 2 phones")


reactions = [
    "https://cdn.discordapp.com/attachments/1157749629706838137/1171230401700823140/live_alf_reaction.jpg?ex=655bec50&is=65497750&hm=10433607a84011d46c1ecb78a9c0d0704f407a0ba4922f87792da43a6344548b&",
    "https://cdn.discordapp.com/attachments/1157749629706838137/1171230402053161081/live_jacib_reaction.jpg?ex=655bec50&is=65497750&hm=bc459cf528e5deab76cef2d84e12c26c8c8781f7ae06ed83fef6a5cc5fa9f916&",
    "https://cdn.discordapp.com/attachments/1157749629706838137/1171230402447417497/live_kettle_reaction.jpg?ex=655bec50&is=65497750&hm=ac9c8b74eee33ccb343cecb28a696c5373cfb131825a39def430b601881c4fa2&",
    "https://cdn.discordapp.com/attachments/1157749629706838137/1171230402950725704/deepfried_ioan.jpg?ex=655bec50&is=65497750&hm=ea2959b4cdd82c48e0a30866fc4ada5151f210b1301c452c6b5fa5d1d4843c53&"
]


def react(reactions, message):
  return message.channel.send(r.choice(reactions))


def kys(message):
  out = ""
  for i in range(100):
    time.sleep(0.2)
    out += 'KILL YOURSELF!!!!!!\n'
    return message.channel.send(out)
