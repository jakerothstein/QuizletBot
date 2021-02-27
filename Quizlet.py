from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#Chrome Window Setup
driver = webdriver.Chrome()
driver.get("https://quizlet.com/")
driver.maximize_window()

#Log In Procces
LogIn = driver.find_element_by_xpath("/html/body/div[3]/div/header/div/div[2]/div[3]/button[1]")
LogIn.click()

uname = driver.find_element_by_name("username")
pword = driver.find_element_by_name("password")

uname.send_keys("Jacob_Rothstein9")
pword.send_keys("PlantCloud9!")

LogInBtn = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/form/button")
LogInBtn.click()

#Navagates to set and inputs the # of sets 
input("Please Navagate to your desired Quizlet and press 'Enter' when ready: ")
crdNum = int(input("What is the number of words in the Quizlet set: "))

#Auto Flashcard program
print("Completing Flashcards")
flshCrd = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div/div/div/div[1]/div/div/div[2]/nav/div/div[1]/span[1]/a/div")
flshCrd.click()

i = 1
while(i <= crdNum):
	arwClc = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div/div[2]/div/div/div[2]/div[2]/span/button/span")
	arwClc.click()
	i += 1
time.sleep(.5)

#back = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div/div[1]/div/aside/div[1]/a")
#back.click()


#driver.quit()