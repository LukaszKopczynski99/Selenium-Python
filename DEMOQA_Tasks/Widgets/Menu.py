from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/menu#")
driver.maximize_window()
driver.implicitly_wait(5)

# ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
# ciacho.click() //coockies may be taken out

Main_item_two= driver.find_element(By.XPATH,"//*[@id='nav']/li[2]/a")
action = ActionChains(driver)
action.move_to_element(Main_item_two).perform()

time.sleep(2)

Sub_sub_list = driver.find_element(By.XPATH,"//*[@id='nav']/li[2]/ul/li[3]/a")
action.move_to_element(Sub_sub_list).perform()

time.sleep(2)

Sub_sub_item_2 = driver.find_element(By.XPATH,"//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")
action.move_to_element(Sub_sub_item_2).perform()
time.sleep(2)

print("Test pass")
driver.quit()