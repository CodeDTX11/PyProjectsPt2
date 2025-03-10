from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

submit_button = driver.find_element(By.CSS_SELECTOR, "form button")

f_name.send_keys("Dylan")
l_name.send_keys("Dilonious")
email.send_keys("diplomatic@gmail.com")

submit_button.click()

# driver.close()