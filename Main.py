from selenium import webdriver

print("Hello from Selenium")

#Navigate to URL
driver = webdriver.Chrome()

#Maximize the Browser Window
driver.maximize_window()

#Find Google Search Box and enter Search text
driver.find_element_by_name("q").send_keys("LinkedIn Login")

#Hit the Submit button on the Search Box
#driver.find_element_by_name("q").send_keys(Keys.Enter )


#driver.find_element_by_partial_link_text("LinkedIn Login").click()

#driver.find_elements("")