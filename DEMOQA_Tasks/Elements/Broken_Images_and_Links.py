import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/broken")
driver.maximize_window()

driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

link = driver.find_element(By.LINK_TEXT, "Click Here for Broken Link").get_attribute("href")
#link = driver.find_element(By.LINK_TEXT, "Click Here for Broken Link").get_attribute("href")

requests_response = requests.head(link)
status_code = requests_response.status_code

if status_code == 200:
    print("Valid link")
else:
    print("Broken link")

print(status_code)
print()

image = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']").get_attribute("src")
#image = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa_1.jpg']").get_attribute("src")

requests_response = requests.head(image)
status_code_v2 = requests_response.status_code

if status_code_v2 == 200:
    print("Valid image")
else:
    print("Broken image")

print(status_code_v2)










driver.quit()
