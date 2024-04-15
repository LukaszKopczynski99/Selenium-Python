from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demoqa.com/links")
driver.implicitly_wait(5)
driver.maximize_window()

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

zwykly_link = driver.find_element(By.LINK_TEXT, "Home")
zwykly_link.click()

time.sleep(3)

dynamiczny_link = driver.find_element(By.XPATH,"//*[@id='dynamicLink']")
kliknij_dynamicznie=WebDriverWait(driver,10).until(EC.element_to_be_clickable(dynamiczny_link))
kliknij_dynamicznie.click()

time.sleep(3)

Created_link = driver.find_element(By.LINK_TEXT, 'Created')
Created_link.click()

time.sleep(5)

driver.quit()