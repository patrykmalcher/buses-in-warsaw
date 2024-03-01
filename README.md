```markdown
# Buses in Warsaw

## Description

The aim of this project is to gather and analyze information about buses in Warsaw.

### Project Structure
The project consists of two main parts:
1. Data Collector
2. Data Analysis

## Data Collector

The Data Collector is a Python-based tool designed to fetch and store data.

### Installation

```bash
make setup
. venv/bin/activate
pip install .
```

### Usage

```python
from datacollector.WarsawAPIFeignClient import WarsawAPIFeignClient
from datacollector.WarsawAPIDataCollector import WarsawAPIDataCollector

# Replace 'YOUR_API_KEY' with your Warsaw API key
api_key = 'YOUR_API_KEY'
client = WarsawAPIFeignClient(api_key)
# Make 10 scrapes 1 second apart
collector = WarsawAPIDataCollector(client, 1, 10)

json_data = collector.scrape()

with open('sample_data.json', 'w') as json_file:
    json_file.write(json_data)
```

## Data Analysis

This part involves processing, analyzing, and visualizing the collected data, done in a Jupyter notebook.

## Code Quality

To maintain code quality, the following checks and fixes are applied:
```bash
python3 -m flake8 src --max-line-length=120 --extend-ignore=E203,E266,E501,W503
autopep8 --recursive --in-place --max-line-length=120 --exclude=".venv" src
```

## Tests

To run tests, execute:
```bash
make test
```

## Profiler

The most CPU-intensive part of the project involves data analysis, particularly in identifying locations with high speeding rates. When run on approximately 200,000 data points, this calculation takes over a minute to complete.
```