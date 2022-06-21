import requests
import os

SHEETY_FLIGHT_ENDPOINT = "SHEETY_FLIGHT_ENDPOINT"
SHEETY_USER_ENDPOINT = "SHEETY_USER_ENDPOINT"


class DataManager:
    def __init__(self):
        self.sheety_flight_data = None
        self.sheety_user_data = None
        self.sheety_put_data = None
        self.get_data()

    def get_data(self):
        sheety_flight_response = requests.get(url=SHEETY_FLIGHT_ENDPOINT)
        sheety_flight_response.raise_for_status()
        sheety_user_response = requests.get(url=SHEETY_USER_ENDPOINT)
        sheety_user_response.raise_for_status()

        self.sheety_flight_data = sheety_flight_response.json()["flightSearch"]
        self.sheety_user_data = sheety_user_response.json()["users"]

    def put_data(self, iata_code, price, city_id, link):
        sheety_put_endpoint = \
            f"{SHEETY_FLIGHT_ENDPOINT}/{city_id}"
        put_params = {
            "flightSearch": {
                "iataCode": iata_code,
                "lowestPrice": price,
                "link": link,
            }
        }
        sheety_response = requests.put(url=sheety_put_endpoint, json=put_params)
        sheety_response.raise_for_status()
        self.sheety_put_data = sheety_response.json()["flightSearch"]

    def get_opportunity(self, min_price):
        self.get_data()
        places_prices_links = {place["city"]: [int(place["lowestPrice"]), place["link"]]
                               for place
                               in self.sheety_flight_data
                               if int(place["lowestPrice"]) <= int(min_price)}
        return places_prices_links
