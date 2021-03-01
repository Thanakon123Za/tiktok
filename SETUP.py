#CREATE BY PRATHOMPORN

#IMPORT
import os
import time
import colorama
from colorama import init
from colorama import Fore, Style

#TITLE PROGRAM
os.system(' title ' +  ' Program Install Libraries ')

print('{}[>] {}Installing Libraries....{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))    
time.sleep(5)
os.system('cls')
print('{}[>] {}Please wait 5 seconds.{}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))    
time.sleep(5)

def installLibraries():

        os.system('pip install selenium')
        os.system('pip install webdriver-manager')
        os.system('pip install bs4')
        os.system('pip install colorama')
        os.system('pip install requests')
        os.system('pip install threading')
        os.system('pip install time')
        os.system('pip install math')
        os.system('pip install Keys')
        os.system('pip install ActionsChains')
        os.system('pip install sys')
        os.system('pip install multiprocessing')
        os.system('pip install logging')
        os.system('pip install glob')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
        #os.system('')
          
if __name__ == "__main__":
    installLibraries()
    os.system('cls')
    print('{}[>] {}All Required Libraries are now installed..{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))   
    time.sleep(3)