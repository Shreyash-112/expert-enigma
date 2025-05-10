from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=opt)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
actual_url=driver.current_url
if expected_url==actual_url:
    print("correct url you can push through")
    # driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
    driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("laptop")
    sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()

    driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
    sleep(2)
else:
    print("recheck it")