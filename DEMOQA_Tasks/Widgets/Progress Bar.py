from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/progress-bar")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

start_Stop_Button = driver.find_element(By.ID,"startStopButton")
start_Stop_Button.click()

read_the_value = driver.find_element(By.XPATH, "//div[@role='progressbar']")
value=read_the_value.text

if value == 50:
    start_Stop_Button.click()
    time.sleep(5)
    start_Stop_Button.click()

if value == 100:
    print("Download complete")
    time.sleep(3)
    start_Stop_Button.click()

time.sleep(20)

