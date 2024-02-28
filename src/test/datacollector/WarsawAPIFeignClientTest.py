import unittest
from unittest.mock import Mock
from src.main.datacollector.WarsawAPIFeignClient import WarsawAPIFeignClient


class WarsawAPIFeignClientTest(unittest.TestCase):
    def setUp(self):
        self.api_key = 'mock'
        self.client = WarsawAPIFeignClient(self.api_key)

    def test_get_bus_data(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 'bus data'}

        with (unittest.mock.patch('requests.get', return_value=mock_response)
              as mock_get):
            response = self.client.get_bus_data()

        mock_get.assert_called_once_with(
            self.client.url,
            params={'apikey': self.api_key,
                    'resource_id': 'f2e5503e-927d-4ad3-9500-4ab9e55deb59',
                    'type': 1}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 'bus data'})


if __name__ == '__main__':
    unittest.main()
