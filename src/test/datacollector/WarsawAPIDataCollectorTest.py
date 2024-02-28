import json
import unittest
from unittest.mock import MagicMock, patch
from src.main.datacollector.WarsawAPIDataCollector import WarsawAPIDataCollector


class TestWarsawAPIDataCollector(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.mock_client.get_bus_data.return_value.status_code = 200
        self.mock_client.get_bus_data.return_value.json.return_value = {
            'result': [{"Time": "2024-02-20 23:54:16", "VehicleNumber": "9411", "Lines": "N64", "Brigade": "1", "Lat": 52.298573, "Lon": 21.012796},
                       {"Time": "2024-02-20 23:21:47", "VehicleNumber": "9950", "Lines": "186", "Brigade": "1", "Lat": 52.278507, "Lon": 20.87541}]
        }
        self.scrape_interval = 1
        self.scrape_count = 1

    @patch('time.sleep', return_value=None)
    @patch('logging.info', return_value=None)
    def test_scrape(self, mock_logging_info, mock_time_sleep):
        collector = WarsawAPIDataCollector(self.mock_client, self.scrape_interval, self.scrape_count)
        result = collector.scrape()

        self.assertEqual(len(json.loads(result)), 2)

    @patch('time.sleep', return_value=None)
    @patch('logging.warn', return_value=None)
    def test_scrape_no_data(self, mock_logging_warn, mock_time_sleep):
        self.mock_client.get_bus_data.return_value.status_code = 404
        collector = WarsawAPIDataCollector(self.mock_client, self.scrape_interval, self.scrape_count)
        result = collector.scrape()

        self.assertEqual(len(json.loads(result)), 0)


if __name__ == '__main__':
    unittest.main()
