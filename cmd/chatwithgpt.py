import openai
import os
import asyncio
import textwrap

# Set up your OpenAI API key
openai.api_key = "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"

# Define a function to send a prompt to ChatGPT and get a response
async def chat(args,message,self):
    if not self.ver:
        return "BOT: i dont wanna run out of api tokens sry. but i might implement other ppls toeks later. "
    # Set up the parameters for the completion request
    
    completions = openai.Completion.create(
        engine="davinci",  # Use the Davinci engine for high-quality responses
        prompt=" ".join(args)+"in english.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    
    for text in textwrap.wrap(completions.choices[0].text,1900):
         await message.channel.send(text)
    
    return False