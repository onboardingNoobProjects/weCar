import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import Logins,Logouts,AddDeals_vars,ToolBar,Index_vars
from requests import get
import helper
import time
import data

class AddDeal(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(AddDeals_vars.addDeal_url)
        helper.login(self)

    def tearDown(self):
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.assertIn('add', self.browser.title)

    def testPageLabels(self):
        for i in AddDeals_vars.addDeal_labels:
            self.assertIn(i, self.browser.page_source)

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

    def testBtSearch(self):
        searchTxt = self.browser.find_element_by_xpath(ToolBar.txtSearch)
        searchTxt.send_keys(ToolBar.carName)

        selected = self.browser.find_element_by_xpath(ToolBar.btSearch)
        selected.click()

        response = self.browser.current_url
        self.assertTrue(response == ToolBar.searched_url + ToolBar.carName)

    def testBtLogout(self):

        helper.logout(self)
        response = self.browser.current_url
        self.assertTrue(response == Index_vars.index_url)

    def testAddDeals(self):

        title = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_title_xpath)
        title.send_keys(AddDeals_vars.addDeal_title)

        details = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_details_xpath)
        details.send_keys(AddDeals_vars.addDeal_details)

        rrp = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_rrp_xpath)
        rrp.send_keys(AddDeals_vars.addDeal_rrp)

        price = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_price_xpath)
        price.send_keys(AddDeals_vars.addDeal_price)

        tippingPoint = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_tippingPoint_xpath)
        tippingPoint.send_keys(AddDeals_vars.addDeal_tippingPoint)

        expiry = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_expiry_xpath)
        expiry.send_keys(AddDeals_vars.addDeal_expiry)

        pic = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_pic_xpath)
        pic.send_keys(AddDeals_vars.addDeal_pic)

        btSubmit = self.browser.find_element_by_xpath(AddDeals_vars.addDeal_btSubmit_xpath)
        btSubmit.click()



    def testPageLoaded(self):
        request = get(data.AddDeals_vars.addDeal_url)
        self.assertEqual(request.status_code, 200)

    # def rrp_tippingPoint_price_inputValidation(self):


if __name__ == '__main__':
    unittest.main(verbosity=2)
