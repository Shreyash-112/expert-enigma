from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://demoapps.qspiders.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//div[text()='Explore more']").click()
sleep(2)
driver.find_element(By.XPATH,"//section[text()='Frames']").click()
sleep(3)
driver.find_element(By.XPATH,"//section[text()='iframes']").click()
sleep(2)


## default
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"username").send_keys("Admin@123")
# driver.find_element(By.ID,"password").send_keys("123456")
# driver.find_element(By.ID,"submitButton").click()

## nested iframe
# driver.find_element(By.XPATH,"//a[text()='Nested iframe']").click()
# sleep(1)
# driver.switch_to.frame(0)
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"email").send_keys("Admin@gmail.com")
# driver.find_element(By.ID,"password").send_keys("Admin@1234")
# driver.find_element(By.ID,"confirm-password").send_keys("Admin@1234")
# driver.find_element(By.ID,"submitButton").click()


## multiple iframe
# driver.find_element(By.XPATH,"//a[text()='Multiple iframe']").click()
# sleep(1)

# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='w-full h-96']"))
#
# driver.find_element(By.ID,"email").send_keys("Admin@gmail.com")
# driver.find_element(By.ID,"password").send_keys("Admin@1234")
# driver.find_element(By.ID,"confirm-password").send_keys("Admin@1234")
# driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()
#
# driver.switch_to.parent_frame()
#
# driver.switch_to.frame(1)
# driver.find_element(By.ID,"username").send_keys("Admin@gmail.com")
# driver.find_element(By.ID,"password").send_keys("Admin@1234")
# driver.find_element(By.XPATH,"//button[text()='Login']").click()


## Nested with Multiple iframe
driver.find_element(By.XPATH,"//a[text()='Nested with Multiple iframe']").click()

# driver.switch_to.frame(0)
# driver.switch_to.frame(driver.find_element(By.XPATH,"(//div[@class='form_container'])[1]/iframe"))
# driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='form-group']/iframe"))
sleep(2)
driver.switch_to.frame(0)
driver.switch_to.frame(0)
driver.switch_to.frame(0)
driver.find_element(By.ID,"email").send_keys("Admin@gmail.com")
driver.switch_to.parent_frame()
driver.switch_to.frame(1)
driver.find_element(By.ID,"password").send_keys("Admin@1234")
driver.switch_to.parent_frame()
driver.switch_to.frame(2)
driver.find_element(By.ID,"confirm").send_keys("Admin@1234")
driver.switch_to.parent_frame()
driver.switch_to.frame(3)
driver.find_element(By.ID,"submitButton").click()

