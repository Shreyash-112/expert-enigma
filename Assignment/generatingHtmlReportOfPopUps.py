from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://demoapps.qspiders.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//div[text()='Explore more']").click()
driver.find_element(By.XPATH,"//section[text()='Frames']").click()
driver.find_element(By.XPATH,"//section[text()='iframes']").click()
