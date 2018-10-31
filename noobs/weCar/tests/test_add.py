import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import logins,logouts,addDeals_vars
import helper
import time

class AddDeal(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(addDeals_vars.addDeal_url)
        helper.login(self)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageLabels(self):
        for i in addDeals_vars.addDeal_labels:
            self.assertIn(i, self.browser.page_source)

    def testBtLogout(self):
        self.browser.get(addDeals_vars.addDeal_url)
        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == 'http://localhost:8000/wecar/')

    def testBtDeals(self):
        selected = self.browser.find_element_by_xpath('//*[@id="topNavBar"]/ul[1]/li[1]/a')
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == 'http://localhost:8000/wecar/')

    def testBtweCar(self):
        selected = self.browser.find_element_by_xpath('/html/body/nav/div/div[1]/a')
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == 'http://localhost:8000/wecar/')

    def testBtSearch(self):
        searchTxt = self.browser.find_element_by_xpath('//*[@id="topNavBar"]/form/div/input')
        carName = 'tesla'
        searchTxt.send_keys('tesla')
        selected = self.browser.find_element_by_xpath('//*[@id="topNavBar"]/form/button')
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == 'http://localhost:8000/wecar/?q=' + 'tesla')



if __name__ == '__main__':
    unittest.main(verbosity=2)
