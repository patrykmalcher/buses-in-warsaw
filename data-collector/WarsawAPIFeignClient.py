import logging
import requests
from common.BusData import BusData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class WarsawAPIFeignClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.um.warszawa.pl/api/action/busestrams_get/'

    def get_bus_data(self):
        parameters = {
            'apikey': self.api_key,
            'resource_id': 'f2e5503e-927d-4ad3-9500-4ab9e55deb59',
            'type': 1,
        }
        response = requests.get(self.url, params=parameters)
        if response.status_code == 200 and isinstance(response.json().get('result'), list):
            result_list = response.json().get('result', [])
            data_class_instances = [BusData(**item) for item in result_list]
            return data_class_instances
        logging.warning('No data in a response.')
        return []
