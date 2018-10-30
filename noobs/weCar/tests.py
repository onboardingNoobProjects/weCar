from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get('localhost:8000/wecar/')
assert 'BMW' in browser.page_source

browser.quit()
