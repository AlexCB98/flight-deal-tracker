import os
import requests

from dotenv import load_dotenv
from flight_data import FlightData


load_dotenv()


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ['SERP_API_KEY']
        self.endpoint = 'https://serpapi.com/search'

    def search_flight(self, origin_airport, destination_airport):
        params = {
            "api_key": self.api_key,
            "engine": "google_flights",
            "departure_id": origin_airport,
            "arrival_id": destination_airport,
            "outbound_date": "2026-08-10",
            "return_date": "2026-08-17",
            "currency": "EUR",
            "hl": "en",
        }