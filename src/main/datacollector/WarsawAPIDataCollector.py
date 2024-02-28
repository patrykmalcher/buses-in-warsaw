import logging
import time
import json
from dataclasses import asdict

from BusData import BusData


class WarsawAPIDataCollector:
    def __init__(self, client, scrape_interval, scrape_count):
        self.client = client
        self.scrape_interval = scrape_interval
        self.scrape_count = scrape_count

    def scrape(self):
        counter = 0
        bus_data = set()

        while counter < self.scrape_count:
            logging.info(f"Scrape {counter + 1}")
            counter += 1

            response = self.client.get_bus_data()

            bus_data_scrape = []

            if (response.status_code == 200 and
                    isinstance(response.json().get('result'), list)):
                result_list = response.json().get('result', [])
                bus_data_scrape = [BusData(**item) for item in result_list]
            else:
                logging.warn("No data in a response.")

            bus_data.update(set(bus_data_scrape))

            time.sleep(self.scrape_interval)

        return json.dumps([asdict(bus_data) for bus_data in list(bus_data)])
