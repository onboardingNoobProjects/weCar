import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login(self):
    inputElement = self.browser.find_element_by_xpath('//*[@id="username"]')
    inputElement.send_keys('ammar')

    inputElement = self.browser.find_element_by_xpath('//*[@id="password"]')
    inputElement.send_keys('pass')

    inputElement.submit()

def logout(self):
    inputElement = self.browser.find_element_by_xpath('//*[@id="topNavBar"]/ul[2]/li/a')
    inputElement.click()
