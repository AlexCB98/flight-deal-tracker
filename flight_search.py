from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        self.prices = {
            'PAR': 120,
            'BER': 80,
            'TYO': 700,
            'LON': 150,
            'ROM': 110,
            'MAD': 140,
            'AMS': 130,
            'VIE': 95,
        }

        self.destinations = {
            'PAR': 'Paris',
            'BER': 'Berlin',
            'TYO': 'Tokyo',
            'LON': 'London',
            'ROM': 'Rome',
            'MAD': 'Madrid',
            'AMS': 'Amsterdam',
            'VIE': 'Vienna',
        }

    def search_flight(self, origin_airport, destination_airport):

        flight_data = FlightData(
            price=self.get_price(destination_airport),
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            destination_city=self.get_destination_name(destination_airport),
            out_date='2026-08-10',
            return_date='2026-08-17',
        )

        return flight_data

    def get_price(self, destination_airport):

        price = self.prices.get(destination_airport, 999)
        return price

    def get_destination_name(self, destination_airport):

        destination = self.destinations.get(destination_airport, 'Unknown')
        return destination