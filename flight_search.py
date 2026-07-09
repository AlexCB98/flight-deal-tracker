from flight_data import FlightData

class FlightSearch:

    def search_flight(self, origin_airport, destination_airport):
        flight_data = FlightData(
            price=120,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            out_date='2026-08-10',
            return_date='2026-08-17',
        )

        return flight_data