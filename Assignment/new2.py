from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(0.5)
driver.find_element(By.XPATH, "//a[contains(text(),'Digital downloads')]").click()
sleep(0.5)
s = driver.find_element(By.ID, "products-orderby")
z = Select(s)
sort = z.options

i = 0
for item in sort:
    z.select_by_index(index=i)
    i += 1
    sleep(0.5)
    s = driver.find_element(By.ID, "products-orderby")
    z = Select(s)
