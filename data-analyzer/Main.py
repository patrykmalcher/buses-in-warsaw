import json
from DataAnalyzer import DataAnalyzer

from common.BusData import BusData

with open('../data.json', 'r') as json_file:
    json_data = json.load(json_file)

bus_data_list = [BusData(**item) for item in json_data]

analyzer = DataAnalyzer(bus_data_list)
analyzer.visualize_speed()