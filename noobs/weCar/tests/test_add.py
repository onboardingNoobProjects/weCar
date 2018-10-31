import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import Logins,Logouts,AddDeals_vars,ToolBar
import helper
import time

class AddDeal(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(AddDeals_vars.addDeal_url)
        helper.login(self)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageLabels(self):
        for i in AddDeals_vars.addDeal_labels:
            self.assertIn(i, self.browser.page_source)

    def testBtDeals(self):
        selected = self.browser.find_element_by_xpath(ToolBar.btDeals)
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == Logins.login_url)

    def testBtweCar(self):
        selected = self.browser.find_element_by_xpath(ToolBar.btweCar)
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == Logins.login_url)

    def testBtSearch(self):
        searchTxt = self.browser.find_element_by_xpath(ToolBar.txtSearch)
        searchTxt.send_keys(Search_vars.carName)

        selected = self.browser.find_element_by_xpath(ToolBar.btSearch)
        selected.click()
        response = self.browser.current_url
        self.assertTrue(response == ToolBar.searched_url + ToolBar.carName)

    def testBtLogout(self):

        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == Logins.login_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)
