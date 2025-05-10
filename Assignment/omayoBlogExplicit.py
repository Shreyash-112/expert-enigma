from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
# driver.implicitly_wait(15)
driver.get("https://omayo.blogspot.com/")

wait=WebDriverWait(driver,30)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[text()='Dropdown']")))
driver.find_element(By.XPATH,"//button[text()='Dropdown']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='Facebook']")))
driver.find_element(By.XPATH,"//a[text()='Facebook']").click()

driver.back()

wait.until(expected_conditions.element_to_be_clickable((By.ID,"timerButton")))
driver.find_element(By.ID,"timerButton").click()

alt=driver.switch_to.alert
print(alt.text)
alt.accept()


