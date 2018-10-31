from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from data import logins
class Dry():

    def login(username,password):
        browser = webdriver.Chrome()
        browser.get(logins.login_url)
        inputElement = browser.find_element_by_xpath(logins.login_username)
        inputElement.send_keys(username)

        inputElement = browser.find_element_by_xpath(logins.login_password)
        inputElement.send_keys(password)

        inputElement.submit()
