from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch


flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()

data = data_manager.get_destination_data()

for destination in data:
    searched_flight = flight_search.search_flight('MUC', destination['iataCode'])

    if searched_flight.price < destination['lowestPrice']:
        notification.send_notification(
            f'Low price alert! Flight from {searched_flight.origin_airport} '
            f'to {searched_flight.destination_airport} costs {searched_flight.price}€.\n'
            f'Departure: {searched_flight.out_date} | Return: {searched_flight.return_date}\n'
        )