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

    def testPageStatusCode(self):
        request = get(data.Register.registerURL)
        self.assertEqual(request.status_code, 200)

    def testPageLoaded(self):
        response = self.browser.current_url
        print("=============="+response)
        self.assertTrue(response == data.Register.registerURL)


class DetailsNoSetUp(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testLoadPageWhileLoggedIn(self):
        self.browser.get(data.Register.loginURL)
        helper.login(self)
        self.browser.get(data.Register.registerURL)
        response = self.browser.current_url
        self.assertFalse(response == data.Register.registerURL)


if __name__ == '__main__':
    unittest.main(verbosity=2)
