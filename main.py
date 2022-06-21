from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
import notification_manager

sheety = DataManager()
sheety_flight_data = sheety.sheety_flight_data
sheety_user_data = sheety.sheety_user_data
data_flight = FlightData(sheety_flight_data, None)

for city in sheety_flight_data:
    city_name = city["city"]
    city_id = city["id"]
    data_flight = FlightData(sheety_flight_data, city_name)
    iata_code = data_flight.iata_code
    data_search_flight = FlightSearch(iata_code, data_flight.date_from, data_flight.date_to)
    flight_price = data_search_flight.lowest_price
    flight_link = data_search_flight.link
    put_sheety_data = sheety.put_data(iata_code, flight_price, city_id, flight_link)

places_prices_links = sheety.get_opportunity(int(notification_manager.MIN_PRICE_NOTIFICATION))

for person in sheety_user_data:
    first_name = person["firstName"]
    email = person["email"]
    notification_manager.NotificationManager(data_flight.date_from, data_flight.date_to,
                                             places_prices_links, first_name, email)
