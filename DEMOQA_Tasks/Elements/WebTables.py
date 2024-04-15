from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/webtables")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()
time.sleep(3)
Dodaj_nowego = driver.find_element(By.ID,"addNewRecordButton")
Dodaj_nowego.click()

Imie = driver.find_element(By.ID, 'firstName')
Imie.send_keys("Lucas")
time.sleep(1)

Nazwisko = driver.find_element(By.ID, "lastName")
Nazwisko.send_keys("C")
time.sleep(1)

Email = driver.find_element(By.ID, "userEmail")
Email.send_keys("LC@op.pl")
time.sleep(1)

Wiek = driver.find_element(By.ID,"age")
Wiek.send_keys(23)
time.sleep(1)

Wyplata = driver.find_element(By.ID,"salary")
Wyplata.send_keys(10000)
time.sleep(1)

Department = driver.find_element(By.ID,"department")
Department.send_keys("none")
time.sleep(1)

Dodawanie = driver.find_element(By.ID, "submit")
Dodawanie.click()

Sortowanie_po_wieku = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]/div[1]")
Sortowanie_po_wieku.click()

time.sleep(3)

print("Test Pass")