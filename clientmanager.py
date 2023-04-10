import os, time
import discord

import settings.settings as set
import settings.style as style
import commands as cme
import robloxtracker

class bot(discord.Client):
  def __init__(self):
    self.oldrblx = {'userPresenceType':-1}
    self.auth = []
    self.blockedservers = []
    self.uptime = time.time()

    print("Loading Verified Users")
    with open('/home/pi/python/utilbot/settings/authusers.txt', 'r') as authlist:
      for user in authlist.readlines():
        self.auth.append(int(user))

    print("Loading Blocked Servers")
    with open('/home/pi/python/utilbot/settings/blockedservers.txt', 'r') as serverlist:
      for user in serverlist.readlines():
        self.blockedservers.append(int(user))

    print("Loaded")
    time.sleep(0.01)

    print("Logging on...")
    super().__init__()

  async def on_ready(self):
    print(f"{style.Fore.GREEN} TOKEN SUCESS")
    time.sleep(0.1)
    os.system('clear')
    print(f'{style.reset} Logged on as {style.user} {self.user}')

    await self.get_channel(1022132262503989313).send(f' UtilBot logged on as {self.user}')

  async def on_message(self, message):
    # print(message.guild.id)
    # print(self.blockedservers)
    # print(message.guild.id in self.blockedservers)

    for item in set.responses:
      if message.guild.id in self.blockedservers:
        break
      if item in message.content.lower():
        await message.reply(set.responses[item])
        print(f"{style.log} sent {style.sent}{set.responses[item]}")
        break
    
    rblx = robloxtracker.game()
    if rblx['userPresenceType']==2 and self.oldrblx['userPresenceType'] != rblx['userPresenceType']:
      await self.change_presence(activity=discord.Game(name=f"Roblox: {rblx['lastLocation']}"))
    self.oldrblx=rblx

    self.ver = True

    if message.content.startswith(set.prefix) and self.ver:
      print(f"{style.log} recieved command {style.command}{message.content} from {style.user}{message.author}")

      m = message.content.split(set.prefix)[1]
      m = m.split(' ')
      cmd = m.pop(0)
      args = m

      try:
        response = await cme.commandlist[cmd](args, message, self)
      except KeyError:
        response = f"HaychBot doesn't know what `{cmd}` is"
      except Exception as error:
        response = f"There was an error: ```{error}```"

      if response != False:
        await message.reply(str(response))
        print(f"{style.log} sent {style.sent}{response}")
    else:
      return

client = bot()
