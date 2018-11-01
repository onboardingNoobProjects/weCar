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
        self.browser.get(data.Index_vars.index_url)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageLoaded(self):
        request = get(data.Index_vars.index_url)
        self.assertEqual(request.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
