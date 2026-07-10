import json


class NotificationManager:

    def send_notification(self, message):

        try:
            with open('flight_deals.json', 'r') as flight_deals:
                data = json.load(flight_deals)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []

        new_deal = {
            'flight_deal': message,
        }

        data.append(new_deal)

        with open('flight_deals.json', 'w') as flight_deals:
            json.dump(data, flight_deals, indent=4)