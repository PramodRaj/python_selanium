from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('Behavior_Production.json'))
    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(10)
        inst.driver.get("https://mytaptrack.com/")
        time.sleep(2)
        inst.driver.find_element_by_class_name("nav-link").click()
        cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input" 
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("parent@mytaptrack.com")
        cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
        # time.sleep(4)
        inst.driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
    # 
    # def setUp(self):
    #     time.sleep(4)
    #     self.driver.get("https://mytaptrack.com/dashboard")


    # def test_1_notification(self):
    #     select = self.testData['notification']
    #     time.sleep(4)
    #     self.preform(select)

    
   
            
    @classmethod
    def tearDownClass(inst):
        time.sleep(4)
        inst.driver.close()
    
    def preform(self,select):
        # time.sleep(1)
        for i in select:
            if i['action'] != "-click-":
                self.driver.find_element_by_css_selector(i['path']).clear()
                self.driver.find_element_by_css_selector(
                    i['path']).send_keys(i['action'])
                time.sleep(0.5)
            else:
                if i['type'] != "link":
                    time.sleep(1)
                    self.driver.find_element_by_xpath(i['path']).click()
                elif i['type'] == "link":
                    self.driver.find_element_by_link_text('New Behavior').click()
                
            time.sleep(2)
        time.sleep(2)



logging.basicConfig(filename="test_behavior.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)






