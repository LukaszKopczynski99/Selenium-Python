from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME,"fc-button-label")
ciacho.click()


full_Name = driver.find_element("id", 'userName')
full_Name.send_keys("Lucas Crush")

Email = driver.find_element("id", 'userEmail')
Email.send_keys("LucasCrush@op.pl")

Curr_Addr = driver.find_element("id", 'currentAddress')
Curr_Addr.send_keys("London")

Perm_Addr = driver.find_element("id", 'permanentAddress')
Perm_Addr.send_keys("Warsaw")

Submit_Button = driver.find_element("id", 'submit')
Submit_Button.click()

time.sleep(5)

print("Pass")

driver.quit()