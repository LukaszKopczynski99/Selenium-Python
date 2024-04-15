from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demoqa.com/dynamic-properties")
driver.implicitly_wait(5)
cookie = driver.find_element(By.CLASS_NAME, "fc-button-label")
cookie.click()

After_Five_Button = driver.find_element(By.ID, "enableAfter")
Dynamic_AFB = WebDriverWait(driver, 10).until(
    (EC.element_to_be_clickable(After_Five_Button)))

Dynamic_AFB.click()

Color_Change = driver.find_element(By.ID, "colorChange")
But_Color_Change = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(Color_Change)
)

But_Color_Change.click()

Vis_Af_Five = driver.find_element(By.ID, "visibleAfter")
But_Vis_af_five = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(Vis_Af_Five)
)
But_Vis_af_five.click()

time.sleep(5)

print("Test pass")

driver.quit()
