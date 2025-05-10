import time

from selenium import webdriver
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://www.royalenfield.com/in/en/home/")
driver.maximize_window()
time.sleep(4)
driver.close()