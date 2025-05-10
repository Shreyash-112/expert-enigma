from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://www.facebook.com/"
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    print("i am in dws page")
else:
    print("im not in dws page")
driver.close()