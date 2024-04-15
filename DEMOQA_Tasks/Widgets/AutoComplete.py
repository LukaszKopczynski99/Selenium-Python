from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/auto-complete")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

Multiple_color = driver.find_element(By.ID, "autoCompleteMultipleInput")
for _ in range(1, 4):
    Multiple_color.send_keys("a")
    Multiple_color.send_keys(Keys.ENTER)

time.sleep(3)

Single_color = driver.find_element(By.ID, "autoCompleteSingleInput")
Single_color.send_keys("a")
Single_color.send_keys(Keys.ARROW_DOWN)
Single_color.send_keys(Keys.ARROW_DOWN)
Single_color.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()
print("Test pass")