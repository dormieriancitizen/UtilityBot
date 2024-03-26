import os, socket, time, subprocess, sys
from datetime import datetime
from colorama import Style, Fore, init
init()

async def execute(args,message,self):
  return "no"

async def ping(args,message,self):
  return "pong"

async def clear(args,message,self):
  if not self.ver:
    return "no"
  os.system("clear")
  print(f'Logged on as{Style.RESET_ALL}{Fore.RED} {self.user} {Style.RESET_ALL}')
  return False

async def source(args,message,self):
  return "https://replit.com/@firedestroyer/UtilBot"

async def rundetails(args,message,self):
  if not self.ver:
    return "No"

  details = {
    "Hostname":socket.gethostname(),
    "IP Address":str(subprocess.check_output(['curl','ifconfig.me'])),
    "Uptime":datetime.utcfromtimestamp(time.time()-self.uptime).strftime('%H:%M:%S'),
  }

  toReturn = ""
  
  for i in details:
    toReturn += i+":"+details[i]+"\n"

  return "```"+toReturn+"```"

async def stop(args,message,self):
  if not self.ver:
    return "no"
  os.system("kill "+str(os.getpid()))

async def restart(args,message,self):
  if not self.ver:
    return "no"
  os.execv(sys.executable, ['python'] + sys.argv)
  os.system("kill "+str(os.getpid()))