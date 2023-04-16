import requests, asyncio

oldrblx={'userPresenceType':-1}
with open("./config/roblox-token.txt",'r') as file:
        token = file.read().rstrip()

def game():
    cookies = {
        '.ROBLOSECURITY':token,
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    json_data = {
        'userIds': [
            171105000,
        ],
    }

    return requests.post('https://presence.roblox.com/v1/presence/users', cookies=cookies, headers=headers, json=json_data).json()['userPresences'][0]

print(game())

async def task(bot):
    rblx = robloxtracker.game()
    if rblx['userPresenceType']==2 and self.oldrblx['userPresenceType'] != rblx['userPresenceType']:
      await bot.change_presence(activity=discord.Game(name=f"Roblox: {rblx['lastLocation']}"))
    elif rblx['userPresenceType']==0 and self.oldrblx['userPresenceType'] != rblx['userPresenceType']:
      await bot.change_presence(activity=None)
    oldrblx=rblx
    await asyncio.sleep(10)