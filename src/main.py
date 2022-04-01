import time
import discord
import requests
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from connexion_selenium import connexion_microsoft_account

####################INITS_VARIABLE####################
options = webdriver.ChromeOptions() 
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

client = discord.Client()
secrets = dotenv_values(".env")
token_discord = secrets["TOKEN_MOULI"]
####################INITS_FUNCTIONS####################

def check_button_logIn():
    try:
        driver.find_element(By.XPATH, value='/html/body/div/div/a/span').click()
    except NoSuchElementException:
        return False
    print("|- Click on the 'Log In'")
    time.sleep(3)
    return True

def search_token(driver):
    driver.refresh()
    time.sleep(3) # page my.epitech.eu
    check_button_logIn()
    token = str(driver.execute_script("return localStorage.getItem('argos-api.oidc-token')"))
    token = token.replace('"', "")
    token = 'Bearer ' + token
    return (requests.get('https://api.epitest.eu/me/2021', headers={'Authorization': token}))

connexion_microsoft_account(driver)
response = search_token(driver)

@client.event
async def on_ready():
    print("Le bot est prêt !")
client.run(token_discord)
