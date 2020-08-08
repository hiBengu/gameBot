from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import random
import os

addr = "/home/bengu/funProjects/geckodriver"

webdriver = webdriver.Firefox(executable_path=addr)
webdriver.get("https://lobby.ikariam.gameforge.com/")
wait = WebDriverWait(webdriver, 30)
print(f"Browser has opened and wait function defined!")

# Waits until button that opens up the login screen, then clicks it
wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]')))
loginSection = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]')
loginSection.click()
print(f"Waited until login section button and then clicked!")

# Find login boxes and Enter email and password
mailAddr = 'testest@test.com.tr'
pwd = 'testtestpassword'

wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/input')))
username = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/input')
username.send_keys(mailAddr)

wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/div/input')))
password = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/div/input')
password.send_keys(pwd)

closeAd = webdriver.find_element_by_xpath('/html/body/div[4]/div[1]/a')
closeAd.click()

loginButton = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/p/button[1]')
loginButton.click()

# Open Last Player
wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button')))
playButton = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button')
playButton.click()

wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[11]/button')))
openServer = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[11]/button')
openServer.click()

print(f"Last played server is opened with mail address: {mailAddr}!")

webdriver.switch_to.window(webdriver.window_handles[1])

wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[16]/div[2]/div[2]/a')))
closeSale = webdriver.find_element_by_xpath('/html/body/div[1]/div[16]/div[2]/div[2]/a')
closeSale.click()

wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accept_btn"]')))
acceptCookie = webdriver.find_element_by_xpath('//*[@id="accept_btn"]')
acceptCookie.click()

sleep(3)
wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[14]/div/div[1]/ul/li[8]/a')))
goDown = webdriver.find_element_by_xpath('/html/body/div[1]/div[14]/div/div[1]/ul/li[8]/a')
goDown.click()

wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="js_CityPosition17Link"]')))
pirateFortress = webdriver.find_element_by_xpath('//*[@id="js_CityPosition17Link"]')
pirateFortress.click()

firstRaid = '/html/body/div[1]/div[16]/div/div[2]/div[2]/div[5]/div/div[1]/table/tbody/tr[1]/td[5]/a'
wait.until(ec.visibility_of_element_located((By.XPATH, firstRaid)))
while(True):
    duration = 0.3  # seconds
    freq = 800  # Hz
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, firstRaid)))
        raid = webdriver.find_element_by_xpath(firstRaid)
        raid.click()
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        randWait = random.randint(160,165)
        sleep(randWait)
    except:
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        sleep(0.1)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        sleep(0.1)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        sleep(0.1)
        captcha = input("Enter Captcha: ")
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="captcha"]')))
        captchaBox = webdriver.find_element_by_xpath('//*[@id="captcha"]')
        captchaBox.send_keys(captcha)

        enterCaptcha = webdriver.find_element_by_xpath('/html/body/div[1]/div[17]/div/div[2]/div[2]/div[4]/div/div[1]/form/div[2]/input')
        enterCaptcha.click()

        randWait = random.randint(160,165)
        sleep(randWait)

sleep(5)
