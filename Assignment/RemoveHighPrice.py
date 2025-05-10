from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
sleep(2)
products=driver.find_elements(By.XPATH,"//input[@value='Add to cart']")
for product in products:
    product.click()
    sleep(2)
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-cart").click()
prices=driver.find_elements(By.XPATH,"//tbody/tr/td[4]/span[2]")
high=0
i=[]
count=1
li=[]
for price in prices:
    li.append(float(price.text))
    if high<li[i]:
        high=li[i]
        count=i+1
    i+=1
    count=str(count)
# driver.find_element(By.XPATH,"(//input[@name='removefromcart'])["+count+"]")
checkbox=driver.find_elements(By.XPATH,"//input[@name='removefromcart']")
checkbox[count-1].click()



