from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('invite_production.json'))
    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(10)
        inst.driver.get("https://mytaptrack.auth.us-west-2.amazoncognito.com/login?response_type=token&client_id=61f7lakgd2mchf12dko1l0mabs&redirect_uri=https://portal.mytaptrack.com/dashboard&state=STATE&scope=openid+profile+aws.cognito.signin.user.admin+email")
        time.sleep(2)
        # inst.driver.find_element_by_class_name("style-jm3xvrt7label").click()
        # cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input" 
        # inst.driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("teacher@mytaptrack.com")
        # cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
        # inst.driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
        # # time.sleep(2)
        # inst.driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
    # 
    def setUp(self):
        time.sleep(7)
        self.driver = webdriver.Chrome()
        # self.driver.get("https://portal.mytaptrack.com/dashboard")
        self.driver.get("https://mytaptrack.auth.us-west-2.amazoncognito.com/login?response_type=token&client_id=61f7lakgd2mchf12dko1l0mabs&redirect_uri=https://portal.mytaptrack.com/dashboard&state=STATE&scope=openid+profile+aws.cognito.signin.user.admin+email")


    def test_1_invite(self):
        select = self.testData['invite']
        time.sleep(2)
        self.preform(select)
    
    def test_2_notification_ignore(self):
        select = self.testData['notification_ignore']
        time.sleep(2)
        self.preform(select)

    def test_3_invite1(self):
        select = self.testData['invite']
        time.sleep(2)
        self.preform(select)

    def test_4_notification_accept(self):
        select = self.testData['notification_accept']
        time.sleep(2)
        self.preform(select)


    def test_5_invite_vreify(self):
        select = self.testData['invite_vreify']
        time.sleep(2)
        self.preform(select)

    @classmethod
    def tearDownClass(inst):
        time.sleep(3)
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
                if i['type'] != 'css':
                    time.sleep(2)
                    self.driver.find_element_by_xpath(i['path']).click()
                else:
                    self.driver.find_element_by_css_selector(i['path']).click()
                    time.sleep(4)
                    

                
            # time.sleep(2)
        time.sleep(2)



logging.basicConfig(filename="invite.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)






