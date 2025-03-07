#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from twilio.rest import Client
import smtplib
import requests
from pprint import pprint

import data_manager

### MUST RUN flight-deal-finder configuration to get environment variables

my_email = "dm5messerly@gmail.com"
test_email = "dylan.messerly@gmail.com"

gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
auth = os.environ["TWIL_AUTH_TOKEN"]

email_on = False

data_manager = data_manager.DataManager()

pprint(data_manager.flight_data.json())

## twilio starting balance: $13.292 starting 03/03/2025
## twilio costs .01 per message
twilio_on = False

if twilio_on:
    account_sid = os.environ.get("TWIL_ACCOUNT_SID")
    auth_token = os.environ["TWIL_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)

    message = client.messages.create(
      body="Hello moto",
      from_='whatsapp:+14155238886',
      to='whatsapp:+15122270252'
    )
    print(message.sid)

elif email_on:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=gmail_app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=test_email,
                            msg=f"Subject:Happy Birthday!")