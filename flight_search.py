from flight_data import FlightData


class FlightSearch:

    def search_flight(self, origin_airport, destination_airport):
        prices = {
            'PAR': 120,
            'BER': 80,
            'TYO': 700,
            'LON': 150,
            'ROM': 110,
            'MAD': 140,
            'AMS': 130,
        }

        price = prices.get(destination_airport, 999)

        flight_data = FlightData(
            price=price,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            out_date='2026-08-10',
            return_date='2026-08-17',
        )

        return flight_data