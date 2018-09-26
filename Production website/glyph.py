from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import logging
class glyphiconTest(unittest.TestCase):
    testData = json.load(open('glyphicon.json'))

    @classmethod
    # initilizes the required data
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(5)
        inst.driver.get("https://mytaptrack.com")

    # def setUp(self):
    #     self.driver.get("https://mytaptrack.com")

    def test_41_fb(self):
        select = self.testData['Test41_fb']
        time.sleep(2)
        self.preform(select)

    # def test_42_instagram(self):
    #     select = self.testData['Test42_instagram']
    #     time.sleep(2)
    #     self.preform(select)
    
    # def test_43_twitter(self):
    #     select = self.testData['Test43_twitter']
    #     time.sleep(2)
    #     self.preform(select)
    
    # def test_44_linkedin(self):
    #     select = self.testData['Test44_linkedin']
    #     time.sleep(2)
    #     self.preform(select)
    
    # def test_45_printerst(self):
    #     select = self.testData['Test45_printerest']
    #     time.sleep(2)
    #     self.preform(select)
    
    # def test_46_terms(self):
    #     select = self.testData['Test46_terms']
    #     time.sleep(2)
    #     self.preform(select)
    
    # def test_47_privacy(self):
    #     select = self.testData['Test47_privacy']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_48_AWS(self):
    #     select = self.testData['AWS']
    #     time.sleep(2)
    #     self.preform(select)

    # def test_49_Logicworks(self):
    #     select = self.testData['Logicworks']
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
                # time.sleep(0.5)
            else:
                self.driver.find_element_by_xpath(i['path']).click()
                # time.sleep(0.5)
        time.sleep(4)


logging.basicConfig(filename="glyph.log", format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
if __name__ == "__main__":
    # its a main method calls setupclass method
    unittest.main(verbosity=1)
