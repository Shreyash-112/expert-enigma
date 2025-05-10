from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://www.dream11.com/")
driver.maximize_window()
sleep(2)
# driver.switch_to.frame("send-sms-iframe")       #by string
# driver.switch_to.frame(0)                       #by index
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='send-sms-iframe']"))            #by webelement ref

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("987456123")


driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element(By.ID,"hamburger").click()

