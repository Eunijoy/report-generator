# data_fetcher.py
import requests
import logging
import random

class DataFetcher:
    def __init__(self, api_url=None):
        # Default to placeholder API if not provided
        self.api_url = api_url or "https://jsonplaceholder.typicode.com/posts"

    def fetch_data(self, rows=10):
        try:
            logging.info(f"Fetching data from {self.api_url}...")
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Limit rows if API returns more than needed
            return data[:rows]
        except Exception as e:
            logging.error(f"API fetch failed: {e}. Generating fallback dummy data...")
            return [
                {"id": i, "title": f"dummy_title_{i}", "body": f"dummy_body_{i}"}
                for i in range(1, rows + 1)
            ]
