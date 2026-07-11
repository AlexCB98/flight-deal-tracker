import sys

from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch


flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()

data = data_manager.get_destination_data()

if not data:
    print('No destinations found.')
    sys.exit()

new_deals_count = 0

for destination in data:
    searched_flight = flight_search.search_flight(
        'MUC',
        destination['iataCode'],
        destination['city'],
    )

    if searched_flight is None:
        print(f"No flights found for {destination['iataCode']}.")
        continue

    if searched_flight.price < destination['lowestPrice']:

        was_saved = notification.send_notification(searched_flight)

        if was_saved:
            new_deals_count += 1
            print('New deal saved.')
        else:
            print('Deal already exists.')

    else:
        print(
            f"No deal for {destination['city']}: "
            f"{searched_flight.price} EUR "
            f"(limit: {destination['lowestPrice']} EUR)"
        )

print(f'New deals found: {new_deals_count}')