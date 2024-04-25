from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPS:
    @staticmethod
    def login():
        # Open page
        driver = webdriver.Chrome()
        driver.get("https://ps.ug.edu.pl/login.web")

        # Logging
        driver.find_element(By.XPATH, "//*[@id='login']").send_keys("280417")
        driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("Ggttwwnn55")
        driver.find_element(By.XPATH, "//*[@id='formLogin']/div[2]/div/button").click()
        time.sleep(3)

        # Go to sign up
        driver.find_element(By.XPATH, "//*[@id='9_zapisyKomunikaty.web']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='4_wdw.web']").click()
        time.sleep(3)

        return driver

