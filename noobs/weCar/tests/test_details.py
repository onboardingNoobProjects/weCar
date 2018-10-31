import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import helper
import data

class Details(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(data.Details.detailsURL)
        helper.login(self)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.assertIn('WeCar', self.browser.title)

    def testImageExists(self):
        elem = self.browser.find_element_by_xpath(data.Details.imageElement)
        self.assertTrue(elem)

    def testH1Exists(self):
        elem = self.browser.find_element_by_xpath(data.Details.titleElement)
        self.assertTrue(elem)

    def testPcExists(self):
        elem = self.browser.find_element_by_xpath(data.Details.titleElement)
        self.assertIn('%', elem.text)

    def testH3Exists(self):
        elem = self.browser.find_element_by_xpath(data.Details.priceElement)
        self.assertTrue(elem)

    def testTippingPointExists(self):
        self.assertIn(data.Details.tippingPoint, self.browser.page_source)

    def testExpiryDateExists(self):
        self.assertIn(data.Details.expiryDate, self.browser.page_source)

    def testDescriptionExists(self):
        elem = self.browser.find_element_by_xpath(data.Details.descriptionElement)
        self.assertTrue(elem)

    def testLogout(self):
        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == data.Details.indexURL)

if __name__ == '__main__':
    unittest.main(verbosity=2)
