```python
from WarsawAPIFeignClient import WarsawAPIFeignClient
from WarsawAPIDataCollector import WarsawAPIDataCollector

api_key = 'YOUR_API_KEY'
client = WarsawAPIFeignClient(api_key)
collector = WarsawAPIDataCollector(client, 1, 10)

json_data = collector.scrape()

with open('sample_data.json', 'w') as json_file:
    json_file.write(json_data)
```