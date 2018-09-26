from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('create_student_production.json'))
    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()#Firefox()#
        inst.driver.implicitly_wait(10)
        inst.driver.get("https://mytaptrack.auth.us-west-2.amazoncognito.com/login?response_type=token&client_id=61f7lakgd2mchf12dko1l0mabs&redirect_uri=https://portal.mytaptrack.com/dashboard&state=STATE&scope=openid+profile+aws.cognito.signin.user.admin+email")
        time.sleep(2)
        # inst.driver.find_element_by_class_name("nav-link").click()
        cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input" 
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("parent@mytaptrack.com")
        cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
        # time.sleep(4)
        inst.driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
    # 
    def setUp(self):
        time.sleep(6)
        self.driver.get("https://portal.mytaptrack.com/dashboard")


    def test_12_create_student(self):
        select = self.testData['create_student']
        time.sleep(4)
        self.preform(select)

    def test_12_create_student_empty_fname(self):
        select = self.testData['create_student_empty_fname']
        time.sleep(4)
        self.preform(select)
    
    def test_13_create_student_empty_lname(self):
        select = self.testData['create_student_empty_lname']
        time.sleep(4)
        self.preform(select)
    
    def test_13_create_student_unselect_role(self):
        select = self.testData['create_student_unselect_role']
        time.sleep(4)
        self.preform(select)
    
    def test_13_create_student_empty_district(self):
        select = self.testData['create_student_empty_district']
        time.sleep(4)
        self.preform(select)

    def test_13_create_student_with_teacher(self):
        select = self.testData['create_student_with_teacher']
        time.sleep(4)
        self.preform(select)
            
    @classmethod
    def tearDownClass(inst):
        time.sleep(5)
        inst.driver.close()
    
    def preform(self,select):
        time.sleep(1)
        for i in select:
            if i['action'] != "-click-":
                self.driver.find_element_by_css_selector(i['path']).clear()
                self.driver.find_element_by_css_selector(
                    i['path']).send_keys(i['action'])
                # time.sleep(0.5)
            elif i['selector_type'] != "xpath" :
                 self.driver.find_element_by_css_selector(i['path']).click()
            else:
                self.driver.find_element_by_xpath(i['path']).click()
                # time.sleep(0.5)
        time.sleep(4)



logging.basicConfig(filename="test_student.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)






