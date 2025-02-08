import os
import sys
import keyboard
import subprocess
import webbrowser
from colorama import Back
from commanding.colors import(R, G, B, Y, C, M, W, D, S)
from commanding.Terminal import(sign, Enter, ERROR, INFO, Information, Working, NotWorking, warning,
                            Complete, successfully, Failed, please, Question, Help, note, other, 
                            Running, Retrying, Ready, Loading, OK, Okay, stop, Critical, paused,
                            Retrying, Skip, SCAN, Chacking, Hacking, security, AI)
from commanding.BackGround import(Red, Green, Blue, Yellow, Cyan, Magenta, White, Black,Dark, Reset)
def clear_screen_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def wsl():
    try:
        clear_screen_terminal()
        if os.name != 'nt':
            print("This script is designed for Windows only.")
            return
        print(fr"""
            {W}•{B}_{W}•      
            {Back.YELLOW}oo{S}{B}|          
           / '\'        
          {Back.YELLOW}({S}{B}\_;/{Back.YELLOW}){S}{B}            
     _ _ _ _____ __    
    | | | |   __|  |   
    | | | |__   |  |__ 
    |_____|_____|_____|{W}""")
        print(f'\n{Back.RED} Windows Subsystem for Linux {S}{W}')
        print(f'{Green} {W}Developer By : Mohammed Al-Baqer {Reset}')
        print(f"{G}[1] {B}Activate (WSL){W}")
        print(f'{sign} for Exit or stop press key {Y}[{R}Ctrl {W}+ {R}C{Y}]{W}')

        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
            print('Exiting...')
            
        subprocess.run("wsl --install", shell=True, check=True)
        print(f"\n{G}[2] {B}View list of distributions (wsl){W}")
        result = subprocess.run("wsl --list --online", shell=True, text=True, capture_output=True)
        print(result.stdout)
        print(f"\n{G}[3] {B}Enter the name of the distribution you want to install Frol (wsl):{W}")
        distro = input(f"{Y}>{W} ").strip()
        print(f"{sign} Installing distribution {W}'{distro}'...")
        subprocess.run(f"wsl --install -d {distro}", shell=True, check=True)
        print(f"\n{sign} Opening a webpage for the selected distribution's environment...{W}")
        distro_links = {
            "Ubuntu": "https://ubuntu.com/wsl",
            "Debian": "https://www.debian.org/",
            "Kali": "https://www.kali.org/",
            "Fedora": "https://getfedora.org/",
            "OpenSUSE": "https://en.opensuse.org/",
            "Alpine": "https://alpinelinux.org/"
        }
        
        if distro in distro_links:
            webbrowser.open(distro_links[distro])
            print(f"{sign} Opened link: {W}{distro_links[distro]}")

        else:
            print(f"{please} No link found for this distribution. Please search manually!{W}")
        print(f"\n{INFO} WSL and your chosen distribution were successfully installed.{W}")

    except subprocess.CalledProcessError as e:
        print(f"{please} An error occurred while executing a command: {e}{W}")

    except Exception as e:
        print(f"{please} An unexpected error occurred: {e}{W}")

def uninstall_wsl():
    remove_wsl = input(f"{Enter} Do you want to uninstall WSL? {Y}(y/n){B}: {Y}").strip().lower()
    
    if remove_wsl == 'y':
        commands = [
            "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force",
            r"tool\UninstallWSL.ps1"
        ]

        for command in commands:
            try:
                result = subprocess.run(
                    ["powershell", "-Command", command],
                    capture_output=True,
                    text=True,       
                    check=True
                )
                print(f"Command executed successfully: {command}")
                print(f"Output:\n{result.stdout}")

            except subprocess.CalledProcessError as e:
                print(f"{Failed} Error executing command: {command}")
                print(f"{Failed} Error message:\n{e.stderr}")

    elif remove_wsl == 'n':
        print(f'{sign} Exit...{W}')
        sys.exit()

    else:
        print(f"{ERROR} input Please enter 'y' or 'n'!{W}")

def main():
    try:
        while True:
            print(rf"""
   {W}•{B}_{W}•
   {Back.YELLOW}oo{S}{B}|
  / '\'
 {Back.YELLOW}({S}{B}\_;/{Back.YELLOW}){S}{B}                
 _ _ _ _____ __    
| | | |   __|  |   
| | | |__   |  |__ 
|_____|_____|_____|              
""")
            print(f'{G}[1] {B}Install WSL{W}')
            print(f'{G}[2] {B}uninstall wsl{W}')
            print(f'{G}[3] {B}Exit{W}')
            choice = input(f'{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}WSL.IQ{R}]─[{G}Enter choice options{R}]\n└──╼ {R}❯{Y}❯{G}❯{B} ')

            if choice == '1':
                clear_screen_terminal()
                wsl()
                break

            elif choice == '2':
                clear_screen_terminal()
                uninstall_wsl()
                break

            elif choice == '3':
                sys.exit()

            else:
                print(ERROR + ' ' + f'the choice False please Try Again !{W}')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    main()
