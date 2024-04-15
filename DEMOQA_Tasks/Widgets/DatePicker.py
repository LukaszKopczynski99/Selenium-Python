from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

pick_date = driver.find_element(By.ID,"datePickerMonthYearInput")
pick_date.click()

pick_month = Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
pick_month.select_by_value('2')

pick_year = Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
pick_year.select_by_value('1999')

pick_day = driver.find_element(By.XPATH,"//div[text()='25']")
pick_day.click()

download_date = pick_date.get_attribute("value")
print(f"Your birthday date is : {download_date}")


#######################################################################
#########################################################################
############################################################################

Sec_date_picker = driver.find_element(By.ID,"dateAndTimePickerInput")
Sec_date_picker.click()

Sec_arrow_month = driver.find_element(By.CLASS_NAME,"react-datepicker__month-read-view--selected-month")
Sec_arrow_month.click()

time.sleep(3)

driver.implicitly_wait(2)

# Sec_month_picker = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-dropdown"))
# Sec_month_picker.select_by_value("3")

#.react-datepicker__month-dropdown > div:nth-child(3)
#


# Sec_arrow_year = driver.find_element(By.CLASS_NAME, "react-datepicker__year-read-view--down-arrow")
# Sec_arrow_year.click()

# Sec_arrow_year_DD = driver.find_element(By.CSS_SELECTOR,".react-datepicker__year-dropdown > div:nth-child(13) ")
# for _ in  range (1, 21):
#     Sec_arrow_year_DD.click()
#
# Sec_pick_year = driver.find_element(By.XPATH,"//div[text()='1999']")
# Sec_pick_year.click()

Sec_day_pick = driver.find_element(By.XPATH,"//div[text()='25']")
Sec_day_pick.click()

time_list = driver.find_elements(By.XPATH,"//ul[@class='react-datepicker__time-list']/li")
for pick_time in time_list:
    if pick_time.text == "08:30":
        pick_time.click()
        break

time.sleep(2)

download_second_date = Sec_date_picker.get_attribute("value")
print(f"Your second date picker birthday is : {download_second_date}")

driver.quit()
print("Test Pass")