from LoginPS import LoginPS
from selenium.webdriver.common.by import By
from datetime import datetime
import time


def signup():
    driver = LoginPS.login()
    driver.find_element(By.XPATH, "//*[@id='tdNazwa10630860_4']").click()
    time.sleep(3)

    # Sing up
    while True:
        if datetime.now().hour == 12 and datetime.now().minute == 56:
            driver.find_element(By.XPATH, "//*[@id='semChooser']").click()
            break

    time.sleep(10)