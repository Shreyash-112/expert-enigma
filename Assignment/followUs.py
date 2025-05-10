from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
fu=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")
for i in fu:
    i.click()
    sleep(2)
    if driver.current_url=="https://demowebshop.tricentis.com/news/rss/1":
        sleep(2)
        driver.back()


















