import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

MY_USERNAME = "username"
MY_PASSWORD = "******"
CHROME_DRIVE_PATH = "C:/Development/chromedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT_URL = "https://www.instagram.com/food_medicine_mk/"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path), options=webdriver.ChromeOptions())

    def login(self):
        self.driver.get(INSTAGRAM_URL)

        sleep(3)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(MY_USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(MY_PASSWORD)

        sleep(2)

        password.send_keys(Keys.ENTER)

        sleep(4)

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT_URL)

        sleep(4)

        followers = self.driver.find_elements(By.CSS_SELECTOR, 'li a')[1]
        followers.click()

        sleep(3)

    def follow(self):
        follow_count = int(self.driver.find_elements(By.CLASS_NAME, '_ac2a')[2].text)
        print(follow_count)
        scroll_down = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(math.ceil(follow_count/12)):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_down)
            sleep(2)
            follow_button = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for button in follow_button:
                print(button.text)
                try:
                    if button.text == "Obserwuj":
                        print("click")
                        button.click()
                        sleep(3)
                except ElementClickInterceptedException:
                    print('You follow ...')
                    pass

        self.driver.quit()


bot = InstaFollower(CHROME_DRIVE_PATH)
bot.login()
bot.find_followers()
bot.follow()
