
from selenium import webdriver


driver = webdriver.Chrome("D:/National_Pen/drivers/chromedriver.exe")
driver.get("http://ec2-18-223-116-199.us-east-2.compute.amazonaws.com")


driver.find_element_by_id('username').send_keys("nitin123")
driver.find_element_by_id('password').send_keys("kronos123")
driver.find_element_by_name('submit').click()
driver.set_page_load_timeout(10)


title = driver.find_element_by_xpath('//*[@id="login"]/h3').text
assert "Dashbord" in title
driver.close()