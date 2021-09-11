import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os  ,shutil ,time
                                                                                
os.system("clear")

print()
print()

logo = """

                        ███████╗████████╗███████╗
                        ██╔════╝╚══██╔══╝██╔════╝
                        ███████╗   ██║   █████╗
                        ╚════██║   ██║   ██╔══╝
                        ███████║   ██║   ██║
                        ╚══════╝   ╚═╝   ╚═╝"""

print()

logo2 = """

           ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
           ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
           ██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
           ██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
           ██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
           ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ """
time.sleep(1)
print(Fore.RED + logo)
time.sleep(1)
print(Fore.GREEN + logo2)

print()

time.sleep(1)
print(Fore.MAGENTA + "\t         [!] Coded By Senuka Thisath Fernando")
time.sleep(1)
print(Fore.MAGENTA + "\t         [!] Member Of Cyber Worriors")
time.sleep(1)
print(Fore.RED + "\t         [!] We Are Not In Danger We Are Danger")
time.sleep(1)

print()
print()
time.sleep(1)
print (Fore.YELLOW + "\t               [1] Evil Eye Banner")
time.sleep(1)
print (Fore.YELLOW + "\t               [2] Neofetch")
time.sleep(1)
print (Fore.YELLOW + "\t               [3] Exit")

print ()
print ()

def evil():
        name = str(input("    [?] Enter Your Name : "))
        cs = str(input("    [?] Enter Cowsay Name : "))
        speed = str(input("    [?] Speed [50 - 150] : "))

        text1 = ("\n\ncowthink -f eyes "+cs+" |lolcat -a --speed="+speed)
        text2 = ("\nfiglet "+name+" |lolcat -a --speed="+speed)
        text3 = ("""
        shopt -s histappend
        \nshopt -s histverify                                                           
        \nexport HISTCONTROL=ignoreboth
        \nPROMPT_DIRTRIM=2
        \nPS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '
        
        \nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        \n\tcommand_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found        }
fi""")

        with open("bash.bashrc","w") as zsh :
                zsh.write(text3)
                zsh.write(text1)
                zsh.write(text2)

def neo():
        name = str(input("       Enter Your Name : "))
        text1 = ("\nneofetch")
        text2 = ("\nfiglet "+name+" |lolcat -a --speed=80")
        text3 = ("""
        shopt -s histappend
        \nshopt -s histverify                                                           
        \nexport HISTCONTROL=ignoreboth
        \nPROMPT_DIRTRIM=2
        \nPS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '
        
        \nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        \n\tcommand_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found        }
fi""")

        with open("bash.bashrc","w") as zsh :
                zsh.write(text3)
                zsh.write(text1)
                zsh.write(text2)

def move_f():
        if os.path.exists("/data/data/com.termux/files/usr/etc/bash.bashrc"):
                os.remove("/data/data/com.termux/files/usr/etc/bash.bashrc")
        if os.path.exists("/data/data/com.termux/files/usr/etc/motd"):
                os.remove("/data/data/com.termux/files/usr/etc/motd")
        shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
        print()
        print()
        print ('\033[31m' + "       Your Banner Has Been Applied. Please Open A New Session")
        print()
        print()
        os.system("                 figlet Done | lolcat")
        print()
        print()

def exit_b():
    print(Fore.MAGENTA + "          [~] Thank You For Choosing STF BANNER")
    os.system("figlet BYE | lolcat --speed=100")
    exit()
time.sleep(1)
cho = int(input("   Enter Your Choice : "))
print ()
if cho == 1 :
        evil()
        move_f()
elif cho == 2:
        neo()
        move_f()                                                                
elif cho == 3:
        exit_b()
