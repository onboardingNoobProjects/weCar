import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import Logins,Logouts,AddDeals_vars,ToolBar,Index_vars
from requests import get
import helper
import time
import data

class indexPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(Index_vars.index_url)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testLoggedIn(self):
        self.browser.get(Logins.login_url)
        helper.login(self)
        elem = self.browser.find_element_by_css_selector('#topNavBar > ul.nav.navbar-nav.navbar-right > li > a')
        self.assertTrue(elem.text == ' Logout' )


    def testPageLoaded(self):
           request = get(data.Index_vars.index_url)
           self.assertEqual(request.status_code, 200)

    def setUp(self):
         self.browser = webdriver.Chrome()
         self.browser.get(data.Index_vars.index_url)

    def tearDown(self):
         self.addCleanup(self.browser.quit)

    def testBtSearch(self):
         searchTxt = self.browser.find_element_by_xpath(ToolBar.txtSearch)
         searchTxt.send_keys(ToolBar.carName)

         selected = self.browser.find_element_by_xpath(ToolBar.btSearch)
         selected.click()

         response = self.browser.current_url
         self.assertTrue(response == ToolBar.searched_url + ToolBar.carName)

    def testBtDeals(self):
         selected = self.browser.find_element_by_xpath(ToolBar.btDeals)
         selected.click()
         response = self.browser.current_url
         self.assertTrue(response == Index_vars.index_url)

    def testBtweCar(self):
         selected = self.browser.find_element_by_xpath(ToolBar.btweCar)
         selected.click()
         response = self.browser.current_url
         self.assertTrue(response == Index_vars.index_url)

    def testBtLogout(self):

        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == Logins.login_url)


if __name__ == '__main__':
    unittest.main(verbosity=2)
