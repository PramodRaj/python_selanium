from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('loginData.json'))

    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Edge()#Firefox()#Chrome()
        inst.driver.implicitly_wait(2)
        inst.driver.get("https://mytaptrack-test.com")

    def setUp(self):
        self.driver = webdriver.Edge()#Chrome()
        self.driver.get("https://mytaptrack-test.com")
        self.driver.find_element_by_class_name("nav-link").click()

    def test_1_login(self):
        select = self.testData['Test1_login']
        time.sleep(2)
        self.preform(select)

    def test_3_invalidpwd(self):
        select = self.testData['Test3_invalidPwd']
        time.sleep(2)
        self.preform(select)

    def test_4_invalidemail(self):
        select = self.testData['Test4_invalidEmail']
        time.sleep(2)
        self.preform(select)

    def test_5_blankemail(self):
        select = self.testData['Test5_blankEmail']
        time.sleep(2)
        self.preform(select)

    def test_6_invalidemailpwd(self):
        select = self.testData['Test6_invalidEmailPwd']
        time.sleep(2)
        self.preform(select)

    def test_9_oldpwd(self):
        select = self.testData['Test9_oldPwd']
        time.sleep(2)
        self.preform(select)

    def test_10_validdetails(self):
        select = self.testData['Test10_validDetails']
        time.sleep(2)
        self.preform(select)
    #
    # def test_12_invalidcode_forgetpwd(self):
    #     select = self.testData['Test12_Invalidcode_ForgetPwd']
    #     time.sleep(2)
    #     self.preform(select)
    #
    # def test_38_invalidemail_forgetpwd(self):
    #     select = self.testData['Test38_InvalidEmail_ForgetPwd']
    #     time.sleep(2)
    #     self.preform(select)

    @classmethod
    def tearDownClass(inst):
        time.sleep(6)
        inst.driver.close()

    def preform(self, select):
        # time.sleep(1)
        for i in select:
            if i['action'] != "-click-":
                self.driver.find_element_by_css_selector(i['path']).clear()
                self.driver.find_element_by_css_selector(
                    i['path']).send_keys(i['action'])
                time.sleep(2)
            else:
                self.driver.find_element_by_css_selector(i['path']).click()
                time.sleep(2)
        time.sleep(4)



logging.basicConfig(filename="Login.log", format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)