import os
from pprint import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):

        flight_deals_bearer_token = os.environ["FLIGHT_DEALS_BEARER_TOKEN"]
        sheety_get_api = "https://api.sheety.co/4b4b124370147e209a1f2e0c2bd5884f/flightDeals/prices"

        sheety_auth_header = {
            "Authorization": f"Bearer {flight_deals_bearer_token}"
        }

        self.flight_data = requests.get(url=sheety_get_api, headers=sheety_auth_header)

        # pprint(response.json())