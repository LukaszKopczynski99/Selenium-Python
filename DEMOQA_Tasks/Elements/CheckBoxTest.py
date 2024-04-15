from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demoqa.com/checkbox")

driver.implicitly_wait(3)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

# Check the checkboxes
check_home = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/span/label")
check_home.click()

print("Test Pass")

time.sleep(3)