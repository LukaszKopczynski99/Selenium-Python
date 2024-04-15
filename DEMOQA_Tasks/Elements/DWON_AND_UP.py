from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/upload-download")

driver.implicitly_wait(5)
driver.maximize_window()
ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

download = driver.find_element(By.ID, "downloadButton")
download.click()

time.sleep(5)

upload = driver.find_element(By.ID, "uploadFile")
upload.send_keys(r"C:\Users\mateu\Desktop\Test.txt")

time.sleep(5)

print("Test Pass")

driver.quit()