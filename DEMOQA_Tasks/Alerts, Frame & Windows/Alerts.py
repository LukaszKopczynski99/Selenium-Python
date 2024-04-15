from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/alerts")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

First_Button = driver.find_element(By.ID, "alertButton")
First_Button.click()
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

time.sleep(3)

Second_Button = driver.find_element(By.ID, "timerAlertButton")
Second_Button.click()
alert2 = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert2.accept()

time.sleep(3)

Third_Button = driver.find_element(By.ID, "confirmButton")
Third_Button.click()
alert3 = WebDriverWait(driver,10).until(EC.alert_is_present())
alert3.dismiss()

time.sleep(3)

Prompt_Button = driver.find_element(By.ID, "promtButton")
Prompt_Button.click()
Prompt_alert = WebDriverWait(driver,10).until(EC.alert_is_present())
Prompt_alert.send_keys("Lucas")
Prompt_alert.accept()

time.sleep(3)


driver.quit()
print("Test Pass")