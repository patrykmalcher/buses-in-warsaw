import requests


class WarsawAPIFeignClient:
    """
    Feign client responsible for communication with the Warsaw external API.

    Attributes:
        api_key (str): API key for accessing the external API.
        url (str): Base URL of the external API.
    """

    def __init__(self, api_key):
        """
        Initializes the WarsawAPIFeignClient instance with the provided API key.

        Args:
            api_key (str): API key for accessing the external API.
        """
        self.api_key = api_key
        self.url = 'https://api.um.warszawa.pl/api/action/busestrams_get/'

    def get_bus_data(self):
        """
        Sends a GET request to the external API and returns the response.

        Returns:
            requests.Response: Response object from the external API.
        """
        parameters = {
            'apikey': self.api_key,
            'resource_id': 'f2e5503e-927d-4ad3-9500-4ab9e55deb59',
            'type': 1,
        }

        return requests.get(self.url, params=parameters)
