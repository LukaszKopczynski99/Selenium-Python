from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(5)

# ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
# ciacho.click()

Select_Value = driver.find_element(By.CSS_SELECTOR,"#withOptGroup > div > div.css-1wy0on6 > div > svg")
Select_Value.click()


time.sleep(3)

# Select_One = driver.find_element(By.ID,"selectOne")
# Select_One.click()
#
# Select_One.send_keys("D")
# Select_One.send_keys(Keys.ENTER)
#
# time.sleep(3)

Old_Style_Select_Menu = driver.find_element(By.ID,"oldSelectMenu")
Old_Style_Select_Menu.click()
select = Select(Old_Style_Select_Menu)
select.select_by_visible_text("Aqua")

time.sleep(3)

Multiselect_drop_down = driver.find_element(By.CSS_SELECTOR,"#selectMenuContainer > div:nth-child(8) > div > div > div > div.css-1wy0on6 > div > svg")
Multiselect_drop_down.click()

time.sleep(3)

Standard_multi_select = driver.find_element(By.ID,"cars")
select2 = Select(Standard_multi_select)
select2.select_by_value('audi')

time.sleep(3)


driver.quit()


