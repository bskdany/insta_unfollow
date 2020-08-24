from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller

import os
import time


class InsagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe') #COPY AND PASTE CHROMEDRIVER.EXE IN THE SAME FOLDER AS THIS PROJECT

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')

        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()  # clicks on the login button
        time.sleep(4)
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div/div/button').click()  # clicks on the Not Now button
        except:
            ""
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()  # clics on the not now button
        time.sleep(2)

        self.driver.get('LINK TO YOUR PROFILE')
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()  # clicks on following
        time.sleep(1)

        self.get_names()

    def get_names(self):

        mouse = Controller()
        mouse.position = (674, 827) #YOU WILL NEED TO CALIBRATE THIS DEPENDING OF YOUR MONITOR, THE CURSOR MUST GO TO THE PAGE DOWN ARROW

        mouse.press(Button.left)
        time.sleep(90)
        mouse.release(Button.left)

        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        time.sleep(3)

        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

        self.whitelist(names)

    def whitelist(self, names):

        for user in names:

            whitelist = ["whitelisted_username","whitelisted_username2"]

            if (user != whitelist):
                self.unfollow(user)

    def unfollow(self, user):
        self.driver.get('https://www.instagram.com/' + user)

        time.sleep(3)

        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button').click()

            time.sleep(3)

            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[1]').click()

            time.sleep(10)

        except:
            print("Error")


if __name__ == '__main__':
    ig_bot = InsagramBot('YOUR USERNAME', 'YOUR PASSWORD')
