
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

driver = webdriver.Chrome("D:/National_Pen/drivers/chromedriver.exe")
driver.get("http://ec2-18-223-116-199.us-east-2.compute.amazonaws.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id('username').send_keys("nitin123")
driver.find_element_by_id('password').send_keys("kronos123")
driver.find_element_by_name('submit').click()

driver.set_page_load_timeout(10)

select = Select(driver.find_element_by_name('city'))
select.select_by_visible_text('CALCUT')
time.sleep(5)

driver.close()


