import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def white_space():
    for _ in range(1, 3):
        print()
        time.sleep(1)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/accordian")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

First_Heading = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "section1Heading")))
First_Heading.click()

Text_First_Heading = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='section1Content']/p")))
Text_First_Heading_receive = Text_First_Heading.text


print("First Heading")
print(Text_First_Heading_receive)

white_space()

Second_Heading = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "section2Heading")))
Second_Heading.click()

Text_Second_Heading_Sec_P = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='section2Content']/p[2]")))
Sec_Text = Text_Second_Heading_Sec_P.text

print("Second Heading - only 2nd paragraph")
print(Sec_Text)

white_space()

Third_Heading = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "section3Heading")))
Third_Heading.click()

Third_text_full = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='section3Content']/p")))
Third_text_receive = Third_text_full.text


print("Third Heading - only 12 letters of the text")
print(Third_text_receive[:12])

white_space()

driver.quit()

print("Test Pass")