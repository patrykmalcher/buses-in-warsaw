import curlify
import requests


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
        headers = {"Cache-Control": "no-cache"}
        response = requests.get(self.url, params=parameters, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
