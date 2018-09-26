from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.set_page_load_timeout(10)
print("hello")
driver.get("http://localhost/")
time.sleep(2)
driver.find_element_by_class_name("nav-link").click()

# name=driver.find_element_by_class_name("form-control")[0].send_keys("parent@myaptrack.com")
cssSelectorOfSameElements = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(3) > input"
driver.find_element_by_css_selector(cssSelectorOfSameElements).send_keys("parent@mytaptrack.com")
#driver.find_element_by_xpath("(//input[@name='username'])[2]").send_keys("parent@myaptrack.com")
cssSelectorOfSameElementsForPwd = "#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > div:nth-child(5) > input"
driver.find_element_by_css_selector(cssSelectorOfSameElementsForPwd).send_keys("Inspire123")
time.sleep(3)
driver.find_element_by_css_selector("#div-forms > div:nth-child(2) > div:nth-child(2) > div > div > form > input.btn.btn-primary.submitButton-customizable").click()#send_keys("keys.ENTER") 
time.sleep(4)
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div > div:nth-child(2) > div:nth-child(18) > div > a").click()
time.sleep(6)
driver.find_element_by_css_selector("#activityRow > div:nth-child(1) > a").click()
time.sleep(6)
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div > div > div:nth-child(2) > div.col-lg-6.col-xl-4.text-center > div > a").click()
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div:nth-child(2) > div > input").send_keys("reading")
time.sleep(6)
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div.dialog-actions.container-fluid > div > div.col-5.col-sm-3.col-xl-2.ml-auto > a").click()
time.sleep(6)
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div > div > div:nth-child(2) > div.col-lg-6.col-xl-4.ng-scope > div > a > i").click()
time.sleep(6)
driver.find_element_by_css_selector("body > div:nth-child(2) > ui-view > div > div > div > div:nth-child(2) > div.col-lg-6.col-xl-4.ng-scope > div > div:nth-child(5) > div:nth-child(1) > a").click()
print("Pass")
time.sleep(4)
driver.quit()
#driver.find_element_by_xpath("(//input[@name='password'])[0]").send_keys("Inspire123")
# rows = driver.find_elements_by_css_selector("form-control inputField-customizable")
# print rows
# driver.find_element_by_class_name("form-control").send_keys("Inspire123")
# driver.find_element_by_name("username").send_keys("parent@mytaptrack.com")
# driver.find_element_by_name("password").send_keys("Inspire123")
# driver.find_element_by_xpath('//*[@id="username"]').send_keys("parent@myaptrack.com")
# driver.find_element_by_xpath('//*[@id="password"]').send_keys("Inspire123")