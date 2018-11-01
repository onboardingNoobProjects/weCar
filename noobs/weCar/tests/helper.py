import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import Logins
from data import Logouts


def login(self):
    inputElement = self.browser.find_element_by_xpath(Logins.login_username)
    inputElement.send_keys(Logins.username)

    inputElement = self.browser.find_element_by_xpath(Logins.login_password)
    inputElement.send_keys(Logins.password)

    inputElement.submit()

def logout(self):
    inputElement = self.browser.find_element_by_xpath(Logouts.logout_bt_path)
    inputElement.click()
