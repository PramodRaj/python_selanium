from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('Data.json'))
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(10)
        inst.driver.get("http://localhost/")
        time.sleep(2)
    
    # def setUp(self):
    #     self.driver.get("http://localhost/dashboard")


    def test_11_login(self):
        self.driver.find_element_by_class_name("nav-link").click()
        cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input" 
        self.driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("parent@mytaptrack.com")
        cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
        self.driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
        # time.sleep(4)
        self.driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
        

    def test_12_create_student(self):
        select = self.testData['create_student']
        time.sleep(4)
        self.preform(select)


    @classmethod
    def tearDownClass(inst):
        time.sleep(5)
        inst.driver.close()
    
    def preform(self,select):
        # time.sleep(1)
        for i in select:
            if i['action'] != "-click-":
                self.driver.find_element_by_css_selector(i['path']).clear()
                self.driver.find_element_by_css_selector(
                    i['path']).send_keys(i['action'])
                # time.sleep(0.5)
            else:
                self.driver.find_element_by_css_selector(i['path']).click()
                # time.sleep(0.5)
        time.sleep(4)



logging.basicConfig(filename="test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    unittest.main(verbosity=1) 






