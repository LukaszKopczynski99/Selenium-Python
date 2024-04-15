from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/slider")
driver.maximize_window()
driver.implicitly_wait(5)

ciacho = driver.find_element(By.CLASS_NAME, "fc-button-label")
ciacho.click()

SliderInside = driver.find_element(By.CSS_SELECTOR, ".range-slider.range-slider--primary")

time.sleep(10)

# action = ActionChains(driver)
# action.drag_and_drop_by_offset(SliderInside,0,0,).perform()

slider_track_width = driver.execute_script("return arguments[0].clientWidth;", SliderInside)

offset_percentage = 0
offset = (slider_track_width / 1) * offset_percentage

action_chains = ActionChains(driver)
action_chains.drag_and_drop_by_offset(SliderInside,offset, 0).perform()

time.sleep(13)


print("Test pass")
driver.quit()







