import json
import unittest
from unittest.mock import MagicMock, patch
from src.main.datacollector.WarsawAPIDataCollector import WarsawAPIDataCollector


class WarsawAPIDataCollectorTest(unittest.TestCase):
    """
    Unit test class for WarsawAPIDataCollector.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.mock_client = MagicMock()
        self.mock_client.get_bus_data.return_value.status_code = 200
        self.mock_client.get_bus_data.return_value.json.return_value = {
            'result': [
                {
                    "Time": "2024-02-20 23:54:16",
                    "VehicleNumber": "9411",
                    "Lines": "N64",
                    "Brigade": "1",
                    "Lat": 52.298573,
                    "Lon": 21.012796
                }
            ]
        }
        self.scrape_interval = 1
        self.scrape_count = 1

    @patch('time.sleep', return_value=None)
    @patch('logging.info', return_value=None)
    def test_scrape(self, mock_logging_info, mock_time_sleep):
        """
        Test the scrape method.
        """
        collector = WarsawAPIDataCollector(self.mock_client,
                                           self.scrape_interval,
                                           self.scrape_count)
        result = collector.scrape()

        self.assertEqual(len(json.loads(result)), 1)

    @patch('time.sleep', return_value=None)
    @patch('logging.warn', return_value=None)
    def test_scrape_no_data(self, mock_logging_warn, mock_time_sleep):
        """
        Test the scrape method when no data is returned.
        """
        self.mock_client.get_bus_data.return_value.status_code = 404
        collector = WarsawAPIDataCollector(self.mock_client,
                                           self.scrape_interval,
                                           self.scrape_count)
        result = collector.scrape()

        self.assertEqual(len(json.loads(result)), 0)

    @patch('time.sleep', return_value=None)
    @patch('logging.info', return_value=None)
    def test_scrape_multiple_times(self, mock_logging_info, mock_time_sleep):
        """
        Test the scrape method when called multiple times.
        """
        self.scrape_count = 2
        self.mock_client.get_bus_data.return_value.json.side_effect = [
            {'result': [
                {"Time": "2024-02-20 23:54:16",
                 "VehicleNumber": "9411",
                 "Lines": "N64",
                 "Brigade": "1",
                 "Lat": 52.298573,
                 "Lon": 21.012796
                 }]
             },
            {'result': [
                {"Time": "2024-02-20 23:54:16",
                 "VehicleNumber": "9411",
                 "Lines": "N64",
                 "Brigade": "1",
                 "Lat": 52.298573,
                 "Lon": 21.012796
                 }]
             },
            {'result': [
                {"Time": "2024-02-20 23:54:16",
                 "VehicleNumber": "9412",
                 "Lines": "N64",
                 "Brigade": "1",
                 "Lat": 52.298573,
                 "Lon": 21.012796
                 }]
             },
            {'result': [
                {"Time": "2024-02-20 23:54:16",
                 "VehicleNumber": "9412",
                 "Lines": "N64",
                 "Brigade": "1",
                 "Lat": 52.298573,
                 "Lon": 21.012796
                 }]
             }
        ]

        collector = WarsawAPIDataCollector(self.mock_client,
                                           self.scrape_interval,
                                           self.scrape_count)
        result = collector.scrape()

        self.assertEqual(len(json.loads(result)), 2)


if __name__ == '__main__':
    unittest.main()
