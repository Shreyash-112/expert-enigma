from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"pollanswers-1").click()
driver.find_element(By.ID,"pollanswers-2").click()
driver.find_element(By.ID,"pollanswers-3").click()
driver.find_element(By.ID,"pollanswers-4").click()
sleep(5)
driver.close()