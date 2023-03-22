import openai
import asyncio, threading

with open("./config/openaitoken.txt",'r') as token:
    lines =  token.readlines()
    openai.api_key = lines[0].rstrip('\n')

async def chat(args,message,self):
    reply = await message.reply("oki thinking")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": " ".join(args)},
        ],
        temperature=0,
    )
    
    await reply.edit(content=response['choices'][0]['message']['content'])
    return False

async def chatedit(args,message,self):
    await message.edit(content="** **")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": " ".join(args)},
        ],
        temperature=0,
    )
    
    await message.edit(content="**This is a message created by ChatGPT: **"+response['choices'][0]['message']['content'])
    return False