import requests, time, math, re, statistics, asyncio

token = ""
with open("./config/token.txt",'r') as file:
   token = file.read().rstrip()

async def search(guild,args):
    while True:
        result = requests.get(f"https://discord.com/api/v9/guilds/{guild}/messages/search?{args}",headers={"authorization":token})

        if result.status_code == 429:
            print(f"Ratelimited for {result.json()['retry_after']}, retrying")
            await asyncio.sleep(int(result.json()["retry_after"]))
        else:
            return result.json()

async def getAllResults(guild,args):
    initResult = await search(guild,args)
    messages = initResult["messages"]

    print(f"{initResult['total_results']} results, iterating {math.ceil(initResult['total_results']/25)} times")

    for i in range(math.ceil(initResult["total_results"]/25)-1):
        messages.extend((await search(guild,f"{args}&offset={(i+1)*25}"))["messages"])

    return(messages)

async def test(args,message,self):
    getAllResults(1022132262503989309, "content=e")
    return "ran"

async def messageCounts(args, message, self):
    guild = message.guild
    counts = {}
    ans = await message.reply("Loading...")
    i =0
    for member in message.guild.members:
        i+=1
        try:
            if len(args) > 0:
                response = await search(guild.id,"author_id="+str(member.id)+"&content="+" ".join(args))
                counts[member.name] = response["total_results"]
            else:
                response = await search(guild.id,"author_id="+str(member.id))
                counts[member.name] = response["total_results"]
            print(f"{member.name} : {counts[member.name]}")
        except IndexError as error:
            counts[member.name] = -1
        try:
            await ans.edit(content=f"Loading... {i}/{len(message.guild.members)}")
        except:
            # Even if the edit gets ratelimited, the script should keep running.
            pass
    
    reply = ""
    for key in sorted(counts, key=counts.get, reverse=True):
        reply += f"- `{key}` has sent `{counts[key]}` messages \n"
    try:
        await ans.edit(content=reply)
    except:
        try:
            await ans.delete()
        except:
            pass
        return reply
    return False

async def channelCounts(args,message,self):
    guild = message.guild
    counts = {}
    ans = await message.reply("Loading...")
    i =0
    for channel in message.guild.text_channels:
        i+=1
        try:
            response = await search(guild.id,"channel_id="+str(channel.id))
            counts[channel.name] = response["total_results"]
            print(f"{channel.name} : {counts[channel.name]}")
        except Exception as error:
            counts[channel.name] = -1
        try:
            await ans.edit(content=f"Loading... {i}/{len(message.guild.text_channels)}")
        except:
            # Even if the edit gets ratelimited, the script should keep running.
            pass
    
    reply = ""
    for key in sorted(counts, key=counts.get, reverse=True):
        reply += f"- The channel `{key}` has `{counts[key]}` messages \n"
    try:
        await ans.edit(content=reply)
    except Exception:
        try:
            await ans.delete()
        except:
            pass
        return reply
    return False

async def miniScoreTracker(args,message,self):
    guild = 1225439877513084928

    response = "## Mini Average Scores \n"

    members = self.get_guild(guild).members

    scoreThingies = {}

    toEdit = await message.reply(f"Loading... 0/{len(members)}")

    i = 0

    for member in members:
        i+=1
        toTrack = member.id
        searchString = f"author_id={toTrack}&channel_id=1225464316736573500&content=https%3A%2F%2Fwww.nytimes.com%2Fbadges%2Fgames%2Fmini.html%3F&has=link"
        responses = await getAllResults(guild, searchString)
        scores = []

        scores = [int(re.search(r'(?<=t=)\d+',item[0]["content"]).group(0)) for item in responses] 
        
        try:
            scoreThingies[member.name] = statistics.fmean(scores)
        except Exception:
            pass
        
        try:
            await toEdit.edit(content=f"Loading... {i}/{len(members)}")
        except:
            # Even if the edit fails, the script should keep loading.
            pass
    
    for key in sorted(scoreThingies, key=scoreThingies.get):
        response += f" - `{key}` has an average mini time of `{round(scoreThingies[key],2)}`s \n"

    try:
        await toEdit.edit(content=response)
    except Exception:
        await asyncio.sleep(3)
        await toEdit.edit(content=response)   
    
    return False