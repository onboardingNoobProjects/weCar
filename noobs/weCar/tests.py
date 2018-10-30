import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Details(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('localhost:8000/wecar/')
        self.assertIn('WeCar', self.browser.title)

    def testPageContents(self):
        self.browser.get('localhost:8000/wecar/')
        self.assertIn('BMW', self.browser.page_source)

if __name__ == '__main__':
    unittest.main(verbosity=2)
