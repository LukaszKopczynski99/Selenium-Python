from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

New_Tab_Button = driver.find_element(By.ID, "tabButton")
New_Tab_Button.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)

New_Window_Button = driver.find_element(By.ID, "windowButton")
New_Window_Button.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])


time.sleep(2)
New_Window_Message_Button = driver.find_element(By.ID, "messageWindowButton")
New_Window_Message_Button.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

driver.quit()

print("Test pass")