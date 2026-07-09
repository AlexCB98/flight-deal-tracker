from flight_data import FlightData

class FlightSearch:

    def search_flight(self, origin_airport, destination_airport):

        if destination_airport == 'PAR':
            price = 120
        elif destination_airport == 'BER':
            price = 80
        elif destination_airport == 'TYO':
            price = 700
        else:
            price = 999

        flight_data = FlightData(
            price=price,
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            out_date='2026-08-10',
            return_date='2026-08-17',
        )

        return flight_data