import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get
import helper
import data

class Details(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(data.Register.registerURL)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageLoaded(self):
        request = get(data.Register.registerURL)
        self.assertEqual(request.status_code, 200)




if __name__ == '__main__':
    unittest.main(verbosity=2)
