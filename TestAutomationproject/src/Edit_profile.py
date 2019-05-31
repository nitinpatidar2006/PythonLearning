
from selenium import webdriver
import time 


lastname = "patidar123"
driver = webdriver.Chrome("D:/National_Pen/drivers/chromedriver.exe")
driver.get("http://ec2-18-223-116-199.us-east-2.compute.amazonaws.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id('username').send_keys("nitin123")
driver.find_element_by_id('password').send_keys("kronos123")
driver.find_element_by_name('submit').click()

driver.set_page_load_timeout(10)

driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()


driver.find_element_by_id('id_last_name').clear()
driver.find_element_by_id('id_last_name').send_keys(lastname)

driver.find_element_by_name('submit').click()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()

time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
result= driver.find_element_by_id('id_last_name').text


time.sleep(1)
driver.close()

