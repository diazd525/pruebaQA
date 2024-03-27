import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

tiempo = 6
s = Service("C:\Driver\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(8)

Username = driver.find_element(By.XPATH, "//input[contains(@name,'username')]")
Username.send_keys("Admin")
time.sleep(tiempo)
password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
password.send_keys("admin123")
time.sleep(tiempo)
botton = driver.find_element(By.XPATH, "//button[@type='submit']")
botton.click()
time.sleep(tiempo)

driver.close()




