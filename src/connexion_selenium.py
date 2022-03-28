import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_info_env import e_get_email, e_get_mdp

def connexion_microsoft_account(driver):
    print("CONNEXION...")
    driver.get('https://my.epitech.eu/index.html#y/2021')
    driver.find_element(By.CLASS_NAME, value='mdl-button__ripple-container').click()
    time.sleep(2)
    driver.find_element(By.NAME, value="loginfmt").send_keys(e_get_email())
    driver.find_element(By.ID, value='idSIButton9').click()
    time.sleep(4)
    driver.find_element(By.NAME, value="Password").send_keys(e_get_mdp())
    driver.find_element(By.ID, value='submitButton').submit()
    time.sleep(1)
    driver.find_element(By.XPATH, value='/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div').click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.url_to_be('https://login.microsoftonline.com/common/SAS/ProcessAuth')
        )
    finally:
        print("CONNECTED !")
        time.sleep(1)
        driver.find_element(By.ID, value='idSIButton9').click()
    time.sleep(1) # page my.epitech.eu
