import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import helper

class Details(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('localhost:8000/wecar/1')
        helper.login(self)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.assertIn('WeCar', self.browser.title)

    def testImageExists(self):
        elem = self.browser.find_element_by_xpath('/html/body/img')
        self.assertTrue(elem)

    def testH1Exists(self):
        elem = self.browser.find_element_by_xpath('/html/body/h1')
        self.assertTrue(elem)

    def testLogout(self):
        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == 'http://localhost:8000/wecar/')

if __name__ == '__main__':
    unittest.main(verbosity=2)
