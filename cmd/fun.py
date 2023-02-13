import random
from colorama import Style, Fore, init
init()

async def rockpaperscissors(args,message,self):
  if not self.ver:
    return "no"
    
  options = [
    "rock",
    "paper",
    "scissors"
  ]
  
  return options[random.randrange(0,2)]