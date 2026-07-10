import json


class NotificationManager:

    def send_notification(self, searched_flight):

        try:
            with open('flight_deals.json', 'r') as flight_deals:
                data = json.load(flight_deals)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []

        new_deal = {
            'origin': searched_flight.origin_airport,
            'destination' : searched_flight.destination_airport,
            'price': searched_flight.price,
            'out_date' : searched_flight.out_date,
            'return_date': searched_flight.return_date,
        }

        if new_deal not in data:
            data.append(new_deal)

            with open('flight_deals.json', 'w') as flight_deals:
                json.dump(data, flight_deals, indent=4)