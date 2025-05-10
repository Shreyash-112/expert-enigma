from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.maximize_window()

driver.get("https://demoapps.qspiders.com/ui?scenario=1")
wait=WebDriverWait(driver,30)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//section[text()='Popups']")))
driver.find_element(By.XPATH,"//section[text()='Popups']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//section[text()='Javascript']")))
driver.find_element(By.XPATH,"//section[text()='Javascript']").click()
driver.implicitly_wait(15)
driver.find_element(By.ID,"buttonAlert2").click()
wait.until(expected_conditions.alert_is_present())
alt=driver.switch_to.alert
alt.accept()
driver.implicitly_wait(15)
driver.find_element(By.XPATH,"//section[text()='Browser Windows']").click()
driver.implicitly_wait(15)
driver.find_element(By.ID,"browserLink1").click()
driver.implicitly_wait(15)
driver.switch_to.window()
driver.implicitly_wait(15)
driver.find_element(By.ID,"email").send_keys("shreyash1@gmail.com")
driver.find_element(By.ID,"password").send_keys("abc@123")
driver.find_element(By.ID,"confirm-password").send_keys("abc@123")
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()
