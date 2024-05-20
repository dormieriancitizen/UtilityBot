import os, time, asyncio
import discord

import settings.settings as set
import settings.style as style
import commands as cme
import robloxtracker

class bot(discord.Client):
  def __init__(self):
    self.auth = []
    self.trustedservers = []
    self.uptime = time.time()

    print("Loading Verified Users")
    with open('/home/pi/python/utilbot/settings/authusers.txt', 'r') as authlist:
      for user in authlist.readlines():
        self.auth.append(int(user))

    print("Loading Allowed Servers")
    with open('/home/pi/python/utilbot/settings/blockedservers.txt', 'r') as serverlist:
      for user in serverlist.readlines():
        self.trustedservers.append(int(user))

    print("Logging on...")
    super().__init__()

  async def on_ready(self):
    print(f"{style.Fore.GREEN} TOKEN SUCESS")
    time.sleep(0.1)
    os.system('clear')
    print(f'{style.reset} Logged on as {style.user} {self.user}')

    await self.get_channel(1022132262503989313).send(f' UtilBot logged on as {self.user}')
    await asyncio.create_task(robloxtracker.task(self))

  async def on_message(self, message):
    # print(message.guild.id)
    # print(self.trustedservers)
    # print(message.guild.id in self.trustedservers)

    self.ver = message.author.id in self.auth

    for item in set.responses:
      try:
        if message.guild.id not in self.trustedservers:
          break
        if item in message.content.lower():
          await message.reply(set.responses[item])
          print(f"{style.log} sent {style.sent}{set.responses[item]}")
          break
      except:
        pass
    try:
      if message.guild.id == 1225439877513084928:
        if "@everyone" in message.content.lower():
          await self.get_channel(1225617311034249347).send(f'```{message.author} sent an @​everyone ping in #{message.channel.name}```')
    except:
      # dm
      pass

    if (message.content.startswith(set.prefix) and self.ver) or message.content.startswith("h!count"):
      print(f"{style.log} recieved command {style.command}{message.content} from {style.user}{message.author}")

      m = message.content.split(set.prefix)[1]
      m = m.split(' ')
      cmd = m.pop(0)
      args = m

      try:
        response = await cme.commandlist[cmd](args, message, self)
      except Exception as error:
        response = f"There was an error: ```{error}```"

      if response != False:
        await message.reply(str(response))
        print(f"{style.log} sent {style.sent}{response}")
    else:
      return

client = bot()
