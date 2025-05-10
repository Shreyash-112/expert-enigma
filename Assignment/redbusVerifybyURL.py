from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://www.redbus.in/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.redbus.in/")
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    print("Correct Url you can push")
else:
    print("Incorrect Url, recheck it")
driver.close()