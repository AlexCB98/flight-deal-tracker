import os
import requests

from dotenv import load_dotenv
from flight_data import FlightData


load_dotenv()


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ['SERP_API_KEY']
        self.endpoint = 'https://serpapi.com/search'

    def search_flight(self, origin_airport, destination_airport, destination_city):
        params = {
            'api_key': self.api_key,
            'engine': 'google_flights',
            'departure_id': origin_airport,
            'arrival_id': destination_airport,
            'outbound_date': '2026-08-10',
            'return_date': '2026-08-17',
            'currency': 'EUR',
            'hl': 'en',
        }

        response = requests.get(
            url=self.endpoint,
            params=params,
            timeout=30,
        )

        response.raise_for_status()
        data = response.json()

        if 'error' in data:
            print(f'API error for {destination_airport}: {data['error']}')
            return None

        flights = data.get('best_flights', [])

        if not flights:
            return None

        cheapest_flight = flights[0]

        for flight in flights:

            if flight['price'] < cheapest_flight['price']:
                cheapest_flight = flight

        flight_segments = cheapest_flight['flights']

        first_segment = flight_segments[0]
        last_segment = flight_segments[-1]

        flight_data = FlightData(
            price=cheapest_flight['price'],
            origin_airport=first_segment['departure_airport']['id'],
            destination_airport=last_segment['arrival_airport']['id'],
            destination_city=destination_city,
            out_date=params['outbound_date'],
            return_date=params['return_date'],
        )

        return flight_data
