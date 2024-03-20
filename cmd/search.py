import requests, time

token = ""
with open("./config/token.txt",'r') as file:
   token = file.read().rstrip()

def search(guild,args):
    while True:
        result = requests.get(f"https://discord.com/api/v9/guilds/{guild}/messages/search?{args}",headers={"authorization":token}).json()

        if "message" in result:
            if "retry_after" in result:
                print(f"Ratelimited for {result['retry_after']}, retrying")
                time.sleep(int(result["retry_after"]))
            else:
                return result
        else:
            print("ran")
            return result


async def messageCounts(args, message, self):
    guild = message.guild
    counts = {}
    ans = await message.reply("loading...")

    for member in message.guild.members:
        try:
            if len(args) > 0:
                response = search(guild.id,"author_id="+str(member.id)+"&content="+" ".join(args))
                counts[member.name] = response["total_results"]
            else:
                response = search(guild.id,"author_id="+str(member.id))
                counts[member.name] = response["total_results"]
            print(f"{member.name} : {counts[member.name]}")
        except IndexError as error:
            counts[member.name] = -1
    reply = ""
    for key in sorted(counts, key=counts.get, reverse=True):
        reply += f"- `{key}` has sent `{counts[key]}` messages \n"
    await ans.edit(content=reply)
    return False