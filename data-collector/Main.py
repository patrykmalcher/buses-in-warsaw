import json
from dataclasses import asdict

from WarsawAPIFeignClient import WarsawAPIFeignClient
from WarsawAPIDataCollector import WarsawAPIDataCollector

api_key = '2d6eb6a3-69a0-4401-95ff-4b2005d24512'
client = WarsawAPIFeignClient(api_key)
collector = WarsawAPIDataCollector(client, 10, 360)
bus_data_list = collector.scrape()

json_data = json.dumps([asdict(bus_data) for bus_data in bus_data_list])

with open('../night_data.json', 'w') as json_file:
    json_file.write(json_data)