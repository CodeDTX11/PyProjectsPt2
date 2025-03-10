from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")

events_sel = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
event_dict = {}

# print(events_sel[0].text)

for i in range( len(events_sel) ):
    temp = events_sel[i].text.split('\n')
    event_dict[i] = {
        'time' : temp[0],
        'name' : temp[1]
    }

print(event_dict)

driver.quit()