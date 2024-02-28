# Buses in Warsaw

---

## Description

Aim of the project is to collect data about buses in Warsaw and analyse them.
<br>
Project is composed of 2 parts:
1. Data collector
2. Data analysis

## Data collector

Data collector can be installed and used within python project.
<br>
It can be used to collect data and save it to the file.

### Installation

TODO

### Usage

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

## Data analysis
Processing, analysing and visualizing the data.
<br>
Done in the notebook. 


---

## Code quality

Checked by `python3 -m flake8 data-collector/`

---

## Tests

TODO

---

## Profiler

TODO