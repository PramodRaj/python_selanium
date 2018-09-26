from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging

class LoginTest(unittest.TestCase):
    testData = json.load(open('AddingActivity_Production.json'))
    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(10)
        inst.driver.get("https://mytaptrack.auth.us-west-2.amazoncognito.com/login?response_type=token&client_id=61f7lakgd2mchf12dko1l0mabs&redirect_uri=https://portal.mytaptrack.com/dashboard&state=STATE&scope=openid+profile+aws.cognito.signin.user.admin+email")
        time.sleep(2)
        # inst.driver.find_element_by_class_name("style-jm3xvrt7label").click()
        cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input" 
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("parent@mytaptrack.com")
        cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
        inst.driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
        # time.sleep(2)
        inst.driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
    # 
    def setUp(self):
        time.sleep(7)
        self.driver.get("https://portal.mytaptrack.com/dashboard")


    def test_1_Add_Activity(self):
        select = self.testData['Add_Activity']
        time.sleep(2)
        self.preform(select)
    
    # def test_2_Add_Activity_kelly(self):
    #     select = self.testData['Add_Activity_kelly']
    #     time.sleep(2)
    #     self.preform(select)
    
    def test_2_Add_Activity_with_empty_starttime(self):
        select = self.testData['Add_Activity_with_empty_starttime']
        time.sleep(2)
        self.preform(select)
    
    def test_3_Add_Activity_with_empty_endtime(self):
        select = self.testData['Add_Activity_with_empty_endtime']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_with_empty_title(self):
        select = self.testData['Add_Activity_with_empty_title']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_woth_empty_comments(self):
        select = self.testData['Add_Activity_with_empty_comments']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_second_time(self):
        select = self.testData['Add_Activity_second_time']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_invalid_timeformat(self):
        select = self.testData['Add_Activity_invalid_timeformat']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_with_wrong_timeDiff(self):
        select = self.testData['Add_Activity_with_wrong_timeDiff']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_with_same_time(self):
        select = self.testData['Add_Activity_with_same_time']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_Activity_valid_second_time(self):
        select = self.testData['Add_Activity_valid_second_time']
        time.sleep(2)
        self.preform(select)
    
    def test_4_Add_2_Activity(self):
        select = self.testData['Add_2_Activity']
        time.sleep(2)
        self.preform(select)
    
    def test_4_deleting_Activity(self):
            select = self.testData['deleting_Activity']
            time.sleep(2)
            self.preform(select)


    def test_4_editing_Activity_with_unfilled_starttime(self):
        select = self.testData['editing_Activity_with_unfilled_starttime']
        time.sleep(2)
        self.preform(select)

    def test_4_editing_Activity_with_unfilled_endtime(self):
        select = self.testData['editing_Activity_with_unfilled_endtime']
        time.sleep(2)
        self.preform(select)

    def test_4_editing_Activity_with_unfilled_title(self):
        select = self.testData['editing_Activity_with_unfilled_title']
        time.sleep(2)
        self.preform(select)

    def test_4_editing_Activity_with_invalidToValid_starttime(self):
        select = self.testData['editing_Activity_with_invalidToValid_starttime']
        time.sleep(2)
        self.preform(select)

    def test_4_editing_Activity_with_invalidToValid_endtime(self):
        select = self.testData['editing_Activity_with_invalidToValid_endtime']
        time.sleep(2)
        self.preform(select)

    # def test_4_editing_added_Activity_starttime_with_invalid_time_Format(self):
    #     select = self.testData['editing_added_Activity_starttime_with_invalid_time_Format']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_4_editing_added_Activity_endtime_with_invalid_time_Format(self):
    #     select = self.testData['editing_added_Activity_endtime_with_invalid_time_Format']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_4_editing_added_Activity_empty_starttime(self):
    #     select = self.testData['editing_added_Activity_empty_starttime']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_4_editing_added_Activity_empty_endtime(self):
    #     select = self.testData['editing_added_Activity_empty_endtime']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_4_editing_added_Activity_empty_title(self):
    #     select = self.testData['editing_added_Activitediting_added_Activity_empty_titley_empty_endtime']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_4_editing_added_Activity_empty_comment(self):
    #     select = self.testData['editing_adediting_added_Activity_empty_commentded_Activitediting_added_Activity_empty_titley_empty_endtime']
    #     time.sleep(2)
    #     self.preform(select)

    



            
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
                time.sleep(2)
                self.driver.find_element_by_xpath(i['path']).click()
                
            # time.sleep(2)
        time.sleep(2)



logging.basicConfig(filename="test_activity_production.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)






