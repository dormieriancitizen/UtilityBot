import time, math
from colorama import init, Fore, Style
init()



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
  
  await message.delete()
  sender = list(msg)
  await message.channel.send('||'+"||||".join(sender)+"||")

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