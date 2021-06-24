# Rock Paper Scissor
# Have Fun!!!
# By neon-l

import random
import time
import sys
from colorama import *
import subprocess

choices =["rock" ,"paper", "scissor"]
score = 0

def banner():
    print("\n")
    print(Fore.LIGHTYELLOW_EX + "       ################################")
    print(Fore.LIGHTYELLOW_EX + "       ##                            ##")
    print(Fore.LIGHTYELLOW_EX + "       ##     ROCK PAPER SCISSOR     ##")
    print(Fore.LIGHTYELLOW_EX + "       ##                            ##")
    print(Fore.LIGHTYELLOW_EX + "       ################################")
    print(Fore.LIGHTCYAN_EX + "\n   By neon-l")
    print(Fore.LIGHTWHITE_EX + "\n  HAVE FUN!! :)")
    print("\n")

#You can change the command "clear" to "cls" on windows
subprocess.call("clear",shell=True)
banner()
while True:
    try:
        u_input=input(Fore.CYAN + "\n [?] Enter 1 to start a game and 2 to check the score : ")
        if u_input == "1":
            user_choice = input(Fore.CYAN + "\n [?] Enter your choice (eg.rock or Rock) : ").lower()
            if user_choice in choices:
                user_choice = user_choice
            else:
                user_choice = input(Fore.MAGENTA + "\n [?] Please enter the correct word again : ").lower()
            bot_choice = (random.choice(choices)).lower()
            print(Fore.YELLOW + "\n [+] Your Choice is       : ",user_choice)
            print(Fore.YELLOW + "\n [+] Computer's Choice is : ",bot_choice)
            if user_choice == bot_choice :
                print(Fore.BLUE + "\n [+] Tie\n")
            elif user_choice == "rock" and bot_choice == "paper":
                print(Fore.LIGHTRED_EX + " [+] Computer Wins and score -1 \n")
                score -= 1
            elif user_choice == "paper" and bot_choice == "scissor":
                print(Fore.LIGHTRED_EX + " [+] Computer Wins and score -1 \n")
                score -= 1
            elif user_choice == "scissor" and bot_choice == "rock":
                print(Fore.LIGHTRED_EX + " [+] Computer Wins and score -1 \n")
                score -= 1
            else:
                print(Fore.GREEN + " [+] You Win and score +1 \n")
                score += 1
        elif u_input == "2":
            if score == 0:
                print (Fore.LIGHTWHITE_EX + " [+] Your score is ",score)
            elif score < 0:
                print (Fore.LIGHTMAGENTA_EX + " [+] Your score is ",score)
            elif score > 0:
                print (Fore.LIGHTGREEN_EX + " [+] Your score is ",score)
    except KeyboardInterrupt:
        print(Fore.RED + "\n [-] Quitting ...")
        time.sleep(1)
        sys.exit()
        