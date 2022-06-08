#!/usr/bin/env python3

# MADE BY SYSKEY#9698

# imports
from datetime import datetime
# get chdir
import os
# http server with livereload
from livereload import Server, shell
# get threading capabilities
import threading
# colors
from colorama import Fore ; from lolpython import lol_py

banner = """
 @@@@@@@  @@@  @@@  @@@ @@@  @@@ @@@@@@@   @@@@@@  @@@      @@@@@@@
 @@!  @@@ @@!  @@!  @@! @@!@!@@@ @@!  @@@ @@!  @@@ @@!        @@!  
 @!@@!@!  @!!  !!@  @!@ @!@@!!@! @!@!@!@  @!@  !@! @!!        @!!  
 !!:       !:  !!:  !!  !!:  !!! !!:  !!! !!:  !!! !!:        !!:  
  :         ::.:  :::   ::    :  :: : ::   : :. :  : ::.: :    :   

$$$$$$$$$$$$$$$$$$$$$$$ The simple hooker $$$$$$$$$$$$$$$$$$$$$$$$
"""

# rainbow banner
lol_py(banner)

# server variables
global port
port = int(input(Fore.LIGHTGREEN_EX + "Port, standard 1337: "))


now = datetime.now()
server_time = now.strftime("%H:%M:%S")

# Start the web server

def start_web():
  print(Fore.CYAN + f"[+] HTTP Server started at localhost [{server_time}]")
  print("Now enjoy your hook and write your favourite JS exploits into the hook :)")
  print(Fore.YELLOW + f"[!] Check so that server is running on: 127.0.0.1:{port}")
  print(Fore.RED + "[!] For the site to run on other devices, use ngrok")
  print(Fore.LIGHTGREEN_EX)

  server = Server()
  server.watch("*")
  server.serve(port=(port), host="127.0.0.1")
  
start_web()




