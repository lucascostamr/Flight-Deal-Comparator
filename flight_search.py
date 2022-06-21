import requests

TEQUILA_SEARCH_ENDPOINT = "TEQUILA_SEARCH_ENDPOINT"
TEQUILA_HEADER = {
    "apikey": "YOUR API KEY"
    }
FLY_FROM_IATA_CODE = "SOME IATA CODE CITY"


class FlightSearch:
    def __init__(self, iata_code, date_from, date_to):
        self.tequila_search_data = None
        self.lowest_price = 0
        self.link = ""
        self.get_data(iata_code, date_from, date_to)

    def get_data(self, iata_code, date_from, date_to):
        tequila_search_params = {
            "fly_from": FLY_FROM_IATA_CODE,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to,
        }
        tequila_search_response = requests.get(
            url=TEQUILA_SEARCH_ENDPOINT,
            params=tequila_search_params,
            headers=TEQUILA_HEADER,
        )
        tequila_search_response.raise_for_status()
        self.tequila_search_data = tequila_search_response.json()
        self.get_price()
        self.get_link()

    def get_price(self):
        prices = [company["price"] for company in self.tequila_search_data["data"]]
        try:
            self.lowest_price = float(min(prices))
        except ValueError:
            pass

    def get_link(self):
        link = [company["deep_link"] for company in self.tequila_search_data["data"]
                if self.lowest_price == float(company["price"])]
        self.link = link[0]
