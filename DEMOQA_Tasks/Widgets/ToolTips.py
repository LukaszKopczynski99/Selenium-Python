from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/tool-tips")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

time.sleep(5) #for website adds

First_button = driver.find_element(By.ID,"toolTipButton")

action = ActionChains(driver)
action.move_to_element(First_button).perform()

time.sleep(3)

Hower_area = driver.find_element(By.ID,"toolTipTextField")
action.move_to_element(Hower_area).perform()

time.sleep(3)

Contrary_word = driver.find_element(By.XPATH, "//a[text()='Contrary']")
action.move_to_element(Contrary_word).perform()

time.sleep(3)

Number_word = driver.find_element(By.XPATH,"//a[(text()='1.10.32')]")
action.move_to_element(Number_word).perform()

time.sleep(3)

driver.quit()