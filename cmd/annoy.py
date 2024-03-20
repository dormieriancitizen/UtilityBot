import time, math, more_itertools, asyncio
from colorama import init, Fore, Style
init()

async def everyone(args,message,self):
  if not self.ver:
    return "nu"
    
  amount = args.pop(0)
  msg = math.floor(1990/len(emojiofpain))*emojiofpain
  await message.channel.send("haha L")
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return "Dun"

async def lag(args,message,self):
  try:
    emojiofpain = args[1]
  except IndexError:
    emojiofpain = "🅰"
  
  if not self.ver:
    return "nu"
  amount = args.pop(0)
  msg = math.floor(1990/len(emojiofpain))*emojiofpain
  await message.channel.send("haha L")
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return "Dun"

async def spam(args,message,self):
  if not self.ver:
    return "haha no all the power is for myself"
  await message.delete()
  amount = args.pop(0)
  msg = " ".join(args)
  for i in range(int(amount)):
    time.sleep(0.1)
    await message.channel.send(msg)
  return False

async def spoil(args,message,self):
  if not self.ver:
    return False
  msg = " ".join(args)
  sender = list(msg)
  await message.edit(content='||'+"||||".join(sender)+"||")
  return False

async def ghostping(args,message,self):
  await message.delete()
  return False

async def allchannelsend(args,message,self):
  if not self.ver:
    return "reaallly not in the mood ty"
      
  for channel in message.guild.text_channels:
    try:
      await channel.send(args[0])
    except:
      pass

  await message.delete()
  return False

async def longmessage(args,message,self):
  if not self.ver:
    return "no"
  with open("./config/longmessage.txt",'r') as scratchfile:
    script =  list(more_itertools.sliced("\n".join(scratchfile.readlines()),1990))
    for i in script:
      await message.channel.send(i)
      asyncio.sleep(0.2)
    await message.delete()
    return False

async def falseeveryone(args,message,self):
  membersend = "" 
  for member in message.guild.members:
            membersend=membersend+member.mention
  await message.delete()
  members =  list(more_itertools.sliced("\n".join(membersend),1990))
  for member in members:
      await message.channel.send(membersend)
  return False

async def untrueeveryone(args,message,self):
  membersend = "" 
  for member in message.guild.members:
            membersend=membersend+"@​"+member.name+"\n"
  await message.delete()
  members =  list(more_itertools.sliced("\n".join(membersend),1990))
  for member in members:
      await message.channel.send(membersend)
  return False