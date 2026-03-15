from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://xqa.io/practice/text-box")

time.sleep(3)

username = driver.find_element(By.ID, "userName")
email = driver.find_element(By.ID, "userEmail")
CurrentAddress = driver.find_element(By.ID, "currentAddress")
PermanentAddress = driver.find_element(By.ID, "permanentAddress")

#Enter Credentials 
username.send_keys("Hello")
email.send_keys("Vikash@123")
CurrentAddress.send_keys("Sommnath")
PermanentAddress.send_keys("Ahmedabad")
submit = driver.find_element(By.ID, "submit") 
submit.click()
time.sleep(2)
output = driver.find_element(By.ID, "output")  # output container
driver.execute_script("window.scrollBy(0, 100);")  # Scrolls 100 pixels down
time.sleep(1)
print(output.text)

driver.quit()
