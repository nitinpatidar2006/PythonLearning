from selenium import webdriver



driver = webdriver.Chrome("D:/National_Pen/drivers/chromedriver.exe")
driver.get("http://ec2-18-223-116-199.us-east-2.compute.amazonaws.com")
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element_by_xpath('//*[@id="register-link"]/a').click()
driver.find_element_by_id('id_username').send_keys("testuser")
driver.find_element_by_id('id_first_name').send_keys("test")
driver.find_element_by_id('id_last_name').send_keys("user")
driver.find_element_by_id('id_email').send_keys("testuser100@gmail.com")
driver.find_element_by_id('id_password1').send_keys("impetus123")
driver.find_element_by_id('id_password2').send_keys("impetus123")
driver.find_element_by_id('id_address').send_keys("indore")
driver.find_element_by_id('id_phone_number').send_keys("+919826932440")
driver.find_element_by_id('id_dob').send_keys("12/12/1985")
driver.find_element_by_id('id_profession').send_keys("QA")
driver.find_element_by_id('id_region_to').send_keys("India")
driver.find_element_by_name('submit').click()

driver.set_page_load_timeout(10)
title = driver.find_element_by_xpath('//*[@id="login"]/h3').text

assert "Dashbord" in title

driver.close()


