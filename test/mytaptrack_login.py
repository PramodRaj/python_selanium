# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MytaptrackLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox("./geckodriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://mytaptrack-test.auth.us-west-2.amazoncognito.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_mytaptrack_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login?response_type=token&client_id=34etd51u9cd4dbnp8pm81374g6&redirect_uri=https://mytaptrack-test.com/dashboard&state=STATE&scope=openid+profile+aws.cognito.signin.user.admin+email")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("parent@mytaptrack.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Inspire123")
        driver.find_element_by_xpath("(//input[@id='username'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='username'])[2]").send_keys("parent@mytaptrack.com")
        driver.find_element_by_xpath("(//input[@id='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='password'])[2]").send_keys("Inspire123")
        driver.find_element_by_xpath("(//input[@name='signInSubmitButton'])[2]").click()
        driver.find_element_by_css_selector("div.text-center.student-selector > a").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text("Logout").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
