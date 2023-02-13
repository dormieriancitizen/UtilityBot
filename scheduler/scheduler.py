import csv, datetime, asyncio, aiohttp, discord

def getSchedule():
  schedule = []
  with open('/home/pi/python/utilbot/scheduler/schedule.csv', mode='r') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
          schedule.append(row)
  return schedule

def getDay(date):
  days = [
    [[9, 26], [10, 27], [11, 30], [12, 31], [3, 13], [4, 17], [12, 22], [13, 23]], 
    [[7, 27], [8, 28], [9], [10], [1,21], [2,22], [3,23], [6,24],], 
    [[9, 22], [10,23], [1,14,24], [2,15,27], [3,16,28], [6,17,29], [7,20,30],[8,21,31]], 
    [[3, 21], [4,24], [5,25], [6,26], [17,27], [18,28],[19],[20] ], 
    [[3, 15, 25], [], [], [], [], [], ], 
    [[7], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
    [[], [], [], [], [], [], ], 
  ]
  
  d = date
  
  count = 0

  for pattern in days[int(d.strftime("%m"))-1]:
    if int(d.strftime("%d")) in pattern:
      print(f"Today is a {'ABCDEFGH'[count]} day")
      dayPattern = count
      break
    count += 1    
  else:
    print("Could not find a valid day for schedule")
    raise ValueError('Could not find a valid day for schedule :). Either on break or dev is lazy.')

  return dayPattern

async def send(*uselesss):
  with open("/home/pi/python/utilbot/scheduler/schedulerwebhook.txt") as file:
    webhookurl = file.read().rstrip()
  
  async with aiohttp.ClientSession() as session:
    webhook = discord.Webhook.from_url(
      webhookurl, adapter=discord.AsyncWebhookAdapter(session))

    e = discord.Embed(title="Today's Schedule",
                      description=f"Your schedule for today ({'ABCDEFGH'[getDay(datetime.datetime.now())]} day).",
                      color=0xdc9afc)
    
    count = 0

    for block in getSchedule()[getDay(datetime.datetime.now())]:
      count += 1
      e.add_field(name=str(count),value=block,inline=False)
      if count > 5:
        break
    e.add_field(name="Flex",value=block,inline=False)

    await webhook.send(embed=e)
  return False

if __name__ == "__main__":
  asyncio.run(send())