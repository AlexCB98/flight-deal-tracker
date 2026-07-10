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
        }

    def search_flight(self, origin_airport, destination_airport, destination_city):

        price = self.prices.get(destination_airport, 999)

        flight_data = FlightData(
            price=price,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            destination_city=destination_city,
            out_date='2026-08-10',
            return_date='2026-08-17',
        )

        return flight_data