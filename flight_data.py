import requests
from datetime import datetime


TEQUILA_LOCATION_ENDPOINT = "YOUR TEQUILA_LOCATION_ENDPOINT"
TEQUILA_HEADER = {
    "apikey": "YOUR API KEY"
}
VACATION_DURATION = 7
MONTHS_AHEAD = 6


class FlightData:
    def __init__(self, sheety_data, city_name):
        self.sheety_data = sheety_data
        self.iata_code = None
        self.date_to = None
        self.date_from = None
        try:
            self.get_iata_code(city_name)
        #     IF THERE'S AN ERROR HERE, JUST GET RID OF THE TYPE EXCEPT ERROR AND PUT JUST EXCEPT:
        except ConnectionError:
            pass

        self.get_date()

    def get_iata_code(self, city_name):
        location_params = {
            "term": city_name,
        }
        tequila_response = requests.get(
            url=TEQUILA_LOCATION_ENDPOINT,
            params=location_params,
            headers=TEQUILA_HEADER
        )
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        self.iata_code = tequila_data["locations"][0]["code"]

    def get_date(self):
        today = datetime.now().strftime("%d/%m/%Y").split("/")
        month = int(today[1]) + MONTHS_AHEAD
        day = int(today[0]) + VACATION_DURATION
        self.date_from = datetime.now().strftime(f"%d/{month}/%Y")
        self.date_to = datetime.now().strftime(f"{day}/{month}/%Y")
