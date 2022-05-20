#Code made by Jake R
srtIcon = '''
   ____          _       _        _     ____          _     ___      ___
  / __ \        (_)     | |      | |   |  _ \        | |   |__ \    / _ \
 | |  | | _   _  _  ____| |  ___ | |_  | |_) |  ___  | |_     ) |  | | | |
 | |  | || | | || ||_  /| | / _ \| __| |  _ <  / _ \ | __|   / /   | | | |
 | |__| || |_| || | / / | ||  __/| |_  | |_) || (_) || |_   / /_  _| |_| |
  \___\_\ \__,_||_|/___||_| \___| \__| |____/  \___/  \__| |____|(_)\___
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
print(srtIcon)
#Chrome Window Setup
driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.get("https://quizlet.com/")
driver.maximize_window()

#Log In Procces
LogIn = driver.find_element_by_xpath("/html/body/div[3]/div/header/div/div[2]/div[3]/button[1]")
LogIn.click()

uname = driver.find_element_by_name("username")
pword = driver.find_element_by_name("password")

uname.send_keys("XXXX") #UPDATE USERNAME
pword.send_keys("XXXX") #UPDATE USER PASSWORD

LogInBtn = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/form/button")
LogInBtn.click()

#Navagates to set and finds the # of sets
input("Please Navagate to your desired Quizlet and press 'Enter' when ready: ")
crdNum = driver.find_element_by_class_name("UIText.UIText--bodyThree")
crdNum = crdNum.text
crdNum = crdNum[2:]
crdNum = int(crdNum)

#Word and Deffintion Scraper
word1 = driver.find_elements_by_class_name("TermText.notranslate.lang-en")
word2 = driver.find_elements_by_class_name("TermText.notranslate.lang-it")

List1 = []
List2 = []

#Putting all the words into their corrasponding lists
print(word1)
print("Scraping List... ")
i = 0
while i < len(word1) - 1:
	List1.append(word1[i].text)
	List2.append(word2[i].text)
	i += 1
print(List1)
print(List2)

time.sleep(3)

#Auto Flashcard program
print("Completing Flashcards")
flshCrd = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div/div/div/div[1]/div/div/div[2]/nav/div/div[1]/span[1]/a/div")
flshCrd.click()

i = 1
arwClc = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/span/button/span")
while(i <= crdNum):
	arwClc.click()
	i += 1

back = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div/div[1]/div/aside/div[1]/a")
back.click()

time.sleep(1)
