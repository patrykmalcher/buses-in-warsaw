import logging
import time
import json
from dataclasses import asdict

from src.main.datacollector.BusData import BusData


class WarsawAPIDataCollector:
    """
    Main class responsible for collecting the data from Warsaw API.

    Attributes:
        client: Feign client used to communicate with the API.
        scrape_interval: Time in seconds between consecutive scrapes.
        scrape_count: Number of scrapes to perform.
    """

    def __init__(self, client, scrape_interval, scrape_count):
        """
        Initializes the WarsawAPIDataCollector instance with the provided parameters.

        Args:
            client: Feign client used to communicate with the API.
            scrape_interval: Time in seconds between consecutive scrapes.
            scrape_count: Number of scrapes to perform.
        """
        self.client = client
        self.scrape_interval = scrape_interval
        self.scrape_count = scrape_count

    def scrape(self):
        """
        Performs scraping of data from the API.

        Returns:
            str: JSON string representing the array of records from all scrapes performed.
        """
        counter = 0
        bus_data = set()

        while counter < self.scrape_count:
            logging.info(f"Scrape {counter + 1}")
            counter += 1

            response = self.client.get_bus_data()
            bus_data_scrape = []

            if response.status_code == 200 and isinstance(response.json().get('result'), list):
                result_list = response.json().get('result', [])
                bus_data_scrape = [BusData(**item) for item in result_list]
            else:
                logging.warning("No data in the response.")

            bus_data.update(set(bus_data_scrape))
            time.sleep(self.scrape_interval)

        return json.dumps([asdict(bus_data) for bus_data in list(bus_data)])
