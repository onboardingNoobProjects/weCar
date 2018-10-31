import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()
# browser.get('localhost:8000/wecar/add')
# inputElement = browser.find_element_by_xpath('//*[@id="username"]')
# inputElement.send_keys('admin')
#
# inputElement = browser.find_element_by_xpath('//*[@id="password"]')
# inputElement.send_keys('pass123')
#
# inputElement.submit()


    # def login(username,password):
    #     browser = webdriver.Chrome()
    #     browser.get('localhost:8000/wecar/add')
    #     inputElement = browser.find_element_by_xpath('//*[@id="username"]')
    #     inputElement.send_keys(username)
    #
    #     inputElement = browser.find_element_by_xpath('//*[@id="password"]')
    #     inputElement.send_keys(password)
    #
    #     inputElement.submit()

class AddDeal(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
        self.browser = webdriver.Chrome()
        self.browser.get('localhost:8000/wecar/add')
        inputElement = self.browser.find_element_by_xpath('//*[@id="username"]')
        inputElement.send_keys(username)

        inputElement = self.browser.find_element_by_xpath('//*[@id="password"]')
        inputElement.send_keys(password)

        inputElement.submit()

    def testusernameTestField(self):
        self.browser.get('localhost:8000/wecar/add')
        self.assertIn('ammar', self.browser.title)


    def testPasswordTextField(self):
        self.browser.get('localhost:8000/wecar/add')
        self.assertIn('pass', self.browser.page_source)

if __name__ == '__main__':
    unittest.main(verbosity=2)
