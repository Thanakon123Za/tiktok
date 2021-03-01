#coding: utf-8
#Create by Prathomporn

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama

def clear():
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    

def logo():
    try:
        text = """                                   
                         ▄▄▄▄▄▄▪  ▄ •▄▄▄▄▄▄▄      ▄ •▄    ▄▄▄▄·      ▄▄▄▄▄▄      
                          •██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪   ▐█ ▀█▪▪     •██        
                           ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·   ▐█▀▀█▄ ▄█▀▄  ▐█.▪     
                           ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌   ██▄▪▐█▐█▌.▐▌ ▐█▌· 
                           ▄██ ▄██·█  █ ▄██  ▀█▄▀▪·█ ▀█▄  ·▀███▀ ▀█▄▀▪ ▄██  \n                    
        """
        bad_colors = ['LIGHTCYAN_EX', 'CYAN']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t                Made by : Prathomporn\n")
    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
start = '/@'
end = '/video/'
views = ' '

boosted_link = input('{}\n[>] {}TikTok Video Link ?: {}'.format(Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET))
username = boosted_link[boosted_link.find(start)+len(start):boosted_link.rfind(end)]
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)
wait = WebDriverWait(driver, 5)
time.sleep(2)

init()
os.system('title ' + ' TikTok Booster - Boost: @{}'.format(username))

def countdown():
    while True:
        time.sleep(10)
        try:
            driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/div/button').click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button')))
            break
        except:
            pass
            continue

def run():
	global views
	global username
	try:
		driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/div/button').click()
		try:
			#bug (Wait for the next patch).
			#views = driver.find_element_by_xpath('').text
			time.sleep(1)
		except:
			pass
		driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
		print('{}[>] {}Successfully Views Sent.{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
		os.system('title ' + ' TikTok Booster ~ Boost: @{}'.format(username))
		#os.system('title ' + ' TikTok Booster ~ Boost: @{} - Views:{}'.format(username, views))
		time.sleep(5)
		countdown()
		run()
	except:
		pass
		run()

def paste_link():
	global boosted_link
	try:
		driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/input').send_keys(boosted_link)
		wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sid4"]/div/div/div/form/div/div/button')))
		run()
	except:
		print('{}\n[X] {}Error.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))

def maximize():
	global maxi
	maxi += 1
	if maxi == 1:
		driver.maximize_window()
	elif maxi >= 1:
		pass
	else:
		pass

def start():
	try:
		driver.get("http://zefoy.com/")
		time.sleep(1)
		while True:
			try:
				wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/h2/span')))
				print('{}\n[X] {}Please Disable Adblock.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
				time.sleep(5)
				continue
			except:
				pass
				break
		while True:
			try:
				maximize()
				wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/div/input[1]')))
				print('{}[>] {}Please do the Captcha.{}'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET))
				time.sleep(3)
				continue
			except:
				pass
				driver.minimize_window()
				break
	except:
		pass
	clear()
	logo()
	print('{}[>] {}Captcha OK.{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
	print('{}[>] {}Please wait 3 seconds. {}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
	time.sleep(3)
	clear()
	logo()
	print('{}[>] {}Starting...{}'.format(Fore.RESET, Fore.LIGHTGREEN_EX, Fore.RESET))
	paste_link()

start()