from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.CLASS_NAME, "ico-login").click()
forget_pass=driver.find_element(By.CSS_SELECTOR,"a[href='/passwordrecovery']")
if forget_pass.is_displayed():
    print("correct url you can push through")
    driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("shreyashbahadure140@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("ABCabc123")
    driver.find_element(By.CSS_SELECTOR,".login-button").click()
    sleep(10)

else:
    print("recheck it")