from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")

my_cookies = driver.find_element(By.ID, "money")

store = driver.find_elements(By.CLASS_NAME, "grayed")

timer_in_seconds = 60 * 5
# end_time = time.time() + timer_in_seconds

end_time = time.time() + 10

start = int(time.time())

for item in store:
    s=item.find_element(By.CSS_SELECTOR, "b")
    print(s.text)

# while time.time() < end_time:
#
#     cookie_button.click()
#
#     if time.time() % 5 < 0.01:
#
#         for item in store[::-1]:
#             if item.get_attribute("class") != "grayed" and int(my_cookies.text) >= :



driver.close()