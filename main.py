import server
import os, sys
from colorama import init
from colorama import Fore, Style

init()

import discord

import clientmanager


def logOn():
  try:
    with open("./config/token.txt",'r') as file:
        token = file.read().rstrip()

    print(f"{Fore.BLUE}CHECKING TOKEN {Style.RESET_ALL}")
    clientmanager.client.run(token)
  except clientmanager.discord.errors.LoginFailure:
    print(f"{Fore.RED}INVALID TOKEN.{Style.RESET_ALL} \n \n \n")

try:
  logOn()
except Exception as Error:
  print(Style.RESET_ALL + "Something went wrong: \n" + Fore.RED + str(Error))

print("Something went very wrong.")
