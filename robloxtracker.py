with open("./config/roblox-token.txt",'r') as file:
        token = file.read().rstrip()

def game():
    import requests

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