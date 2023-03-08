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
            {"role": "user", "content": args[0]},
        ],
        temperature=0,
    )
    
    await reply.edit(content=response['choices'][0]['message']['content'])
    return False