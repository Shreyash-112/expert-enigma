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
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[2]/div/ul/li[1]/a").click()
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div/label").click()
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input[1]").send_keys("Shreyash")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input[1]").send_keys("Bahadure")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input[1]").send_keys("shreyashbahadure40@gmail.com")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/input[1]").send_keys("ABCabc123")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input[1]").send_keys("ABCabc123")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[4]/input").click()

else:
    print("wrong Url recheck it")
time.sleep(10)