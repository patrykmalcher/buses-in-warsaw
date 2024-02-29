from WarsawAPIFeignClient import WarsawAPIFeignClient
from WarsawAPIDataCollector import WarsawAPIDataCollector
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

api_key = '2d6eb6a3-69a0-4401-95ff-4b2005d24512'
client = WarsawAPIFeignClient(api_key)
collector = WarsawAPIDataCollector(client, 5, 720)

json_data = collector.scrape()

with open('../../../notebook/data/2.30-3.30.json', 'w') as json_file:
    json_file.write(json_data)
