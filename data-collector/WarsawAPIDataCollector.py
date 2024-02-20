import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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

            bus_data.update(set(self.client.get_bus_data()))

            time.sleep(self.scrape_interval)

        return list(bus_data)
