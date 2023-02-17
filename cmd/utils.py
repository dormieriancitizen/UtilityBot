import asyncio, discord, aiohttp
from colorama import init, Fore, Style

init()


async def echo(args, message, self):
  if not self.ver:
    answer = f"{message.author.mention} ran a command and {self.user.mention} bears no responsiblity \n {' '.join(args)}"
  else:
    answer = ' '.join(args)
  return (answer)


async def nuke(args, message, self):
  if self.ver:
    messages = await message.channel.history(limit=int(args[0]) + 1).flatten()
    messages.pop(0)
    for toDel in messages:
      try:
        await asyncio.sleep(0.3)
        await toDel.delete()
      except:
        print(f"{Fore.RED} Attempted to permlesss nuke {Style.RESET_ALL}")
  else:
    return ("nah don't feel like it")
  
  await message.delete()
  return False


async def sendembed(args, message, self):
  if not self.ver:
    return "no"
  print(args)
  i = 0
  for arg in args:
    args[i] = arg.replace("-", " ")
    i += 1
  async with aiohttp.ClientSession() as session:
    webhook = discord.Webhook.from_url(
      args[0], adapter=discord.AsyncWebhookAdapter(session))

    e = discord.Embed(title=args[1],
                      description=args[2],
                      color=0xdc9afc)

    i = 3
    while True:
      try:
        e.add_field(name=args[i], value=args[i + 1])
      except:
        break
      i += 2

    await webhook.send(embed=e)

  await message.delete()

async def status(args,message,self):
  if not self.ver:
    return "no"
  activity = discord.Game(name=' '.join(args))
  await self.change_presence(status=discord.Status.online, activity=activity)
  await message.delete()
  return False