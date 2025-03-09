import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

my_email = "dm5messerly@gmail.com"
test_email = "dylan.messerly@gmail.com"

load_dotenv()

gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")

dollar_tag = soup.find(name="span", class_="a-price-whole")
cent_tag = soup.find(name="span", class_="a-price-fraction")

price = float(dollar_tag.text + cent_tag.text)

# Get the product title
title = soup.find(id="productTitle").getText()

title = title.split()
title = " ".join(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 10

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=gmail_app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=test_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))