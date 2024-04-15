from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

Small_modal_button = driver.find_element(By.ID, "showSmallModal")
Small_modal_button.click()

time.sleep(1)

# Close_small_modal = driver.find_element(By.ID, "closeSmallModal")
# Close_small_modal.click()

#using X sign to close

Close_small_modal_x = driver.find_element(By.CSS_SELECTOR, ".modal-header button span:nth-child(1)")
Close_small_modal_x.click()


time.sleep(2)

Large_modal_button = driver.find_element(By.ID, "showLargeModal")
Large_modal_button.click()

time.sleep(1)

Close_large_modal = driver.find_element(By.ID, "closeLargeModal")
Close_large_modal.click()

time.sleep(2)

driver.quit()
print("Test Pass")