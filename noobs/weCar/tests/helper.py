import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import logins
from data import logouts

def login(self):
    inputElement = self.browser.find_element_by_xpath(logins.login_username)
    inputElement.send_keys('ammar')

    inputElement = self.browser.find_element_by_xpath(logins.login_password)
    inputElement.send_keys('pass')

    inputElement.submit()

def logout(self):
    inputElement = self.browser.find_element_by_xpath(logouts.logout_bt)
    inputElement.click()
