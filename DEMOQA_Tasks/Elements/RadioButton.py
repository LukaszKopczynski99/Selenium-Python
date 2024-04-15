from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/radio-button")

driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()
print("Przed")

Button_YES_status = driver.find_element(By.ID,"yesRadio").is_selected()
print(Button_YES_status)

Button_Yes_click = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[2]/label")
Button_Yes_click.click()

print("Po")

Button_YES_status = driver.find_element(By.ID,"yesRadio").is_selected()
print(Button_YES_status)

time.sleep(5)

Button_Impressive = driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label")
Button_Impressive.click()

time.sleep(5)

driver.quit()