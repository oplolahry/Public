import pyautogui
import time
import os

class color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BACK = '\033[1A'

print(fr"""{color.CYAN} 

     ▒█████   ██▓███   ██▓     ▒█████   ██▓    ▄▄▄       ██░ ██  ██▀███ ▓██   ██▓
    ▒██▒  ██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒   ▒████▄    ▓██░ ██▒▓██ ▒ ██▒▒██  ██▒
    ▒██░  ██▒▓██░ ██▓▒▒██░    ▒██░  ██▒▒██░   ▒██  ▀█▄  ▒██▀▀██░▓██ ░▄█ ▒ ▒██ ██░
    ▒██   ██░▒██▄█▓▒ ▒▒██░    ▒██   ██░▒██░   ░██▄▄▄▄██ ░▓█ ░██ ▒██▀▀█▄   ░ ▐██▓░
    ░ ████▓▒░▒██▒ ░  ░░██████▒░ ████▓▒░░██████▒▓█   ▓██▒░▓█▒░██▓░██▓ ▒██▒ ░ ██▒▓░
    ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒▓ ░▒▓░  ██▒▒▒ 
      ░ ▒ ▒░ ░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒   ▒▒ ░ ▒ ░▒░ ░  ░▒ ░ ▒░▓██ ░▒░ 
    ░ ░ ░ ▒  ░░         ░ ░   ░ ░ ░ ▒    ░ ░    ░   ▒    ░  ░░ ░  ░░   ░ ▒ ▒ ░░  
        ░ ░               ░  ░    ░ ░      ░  ░     ░  ░ ░  ░  ░   ░     ░ ░     
                                                                         ░ ░
{color.RESET}""")

print("You need to download these modeules: pyautogui")
print("Download modules with: pip install module_name")

#b = str(input("Enter message: "))
e = (input("How many times: "))
print("You have 4 seconds")

time.sleep(4)

for i in range (0, int(e)):
    newpath = fr'C:\Users\dkovarik\Desktop\Ahoj{i}'
    os.makedirs(newpath)
