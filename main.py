from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch


flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()

data = data_manager.get_destination_data()

new_deals_count = 0

for destination in data:
    searched_flight = flight_search.search_flight(
        'MUC',
        destination['iataCode'],
    )

    if searched_flight.price < destination['lowestPrice']:

        was_saved = notification.send_notification(searched_flight)

        if was_saved:
            new_deals_count += 1
            print('New deal saved.')
        else:
            print('Deal already exists.')

print(f'New deals found: {new_deals_count}')