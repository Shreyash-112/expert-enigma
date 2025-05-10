import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=options)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(5)
actual_url=driver.current_url
if expected_url==actual_url:
    print("correct url you can push through")
    driver.find_element(By.CLASS_NAME,"ico-register").click()
    driver.find_element(By.ID,"gender-male").click()
    driver.find_element(By.ID,"FirstName").send_keys("Shreyash")
    driver.find_element(By.ID,"LastName").send_keys("Bahadure")
    driver.find_element(By.ID,"Email").send_keys("shreyashbahadure140@gmail.com")
    driver.find_element(By.ID,"Password").send_keys("ABCabc123")
    driver.find_element(By.ID,"ConfirmPassword").send_keys("ABCabc123")
    driver.find_element(By.ID,"register-button").click()

else:
    print("wrong Url recheck it")
time.sleep(10)



