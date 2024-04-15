from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#DOUBLE CLICK

driver.get("https://demoqa.com/buttons")

driver.implicitly_wait(5)

cookie = driver.find_element(By.CLASS_NAME, "fc-button-label")
cookie.click()

driver.maximize_window()
Double_click_button = driver.find_element(By.ID,'doubleClickBtn')
actions = ActionChains(driver)
actions.double_click(Double_click_button).perform()

time.sleep(5)

#Right Click
Right_click_button = driver.find_element(By.ID,'rightClickBtn')
actions2=ActionChains(driver)
actions2.context_click(Right_click_button).perform()

time.sleep(5)

#DynClick
Just_click_button = (By.XPATH, "//button[text()='Click Me']")
dynamic_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(Just_click_button)
)

dynamic_button.click()

time.sleep(5)

driver.quit()