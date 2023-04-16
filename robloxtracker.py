import requests, asyncio, discord

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

async def task(bot):
    oldrblx={'userPresenceType':-1}
    while True:
        rblx = game()

        if rblx['userPresenceType']==2 and oldrblx['userPresenceType'] != rblx['userPresenceType']:
            await bot.change_presence(activity=discord.Game(name=f"Roblox: {rblx['lastLocation']}"))
        elif (rblx['userPresenceType']==1 or rblx['userPresenceType']==0) and oldrblx['userPresenceType'] != rblx['userPresenceType']:
            await bot.change_presence(activity=None)
        
        oldrblx=rblx
        await asyncio.sleep(10)