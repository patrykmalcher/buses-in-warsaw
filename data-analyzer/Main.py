import json

from folium import folium
from folium.plugins import HeatMap

from DataAnalyzer import DataAnalyzer

from common.BusData import BusData

with open('../night_data.json', 'r') as json_file:
    json_data = json.load(json_file)

bus_data_list = [BusData(**item) for item in json_data]

analyzer = DataAnalyzer(bus_data_list)
how_many, points = analyzer.buses_exceeding_50()

warsaw_coordinates = (52.2297, 21.0122)

# Create a map centered around Warsaw
map_warsaw = folium.Map(location=warsaw_coordinates, zoom_start=12)

# Create heatmap data
heat_data = [[point[0], point[1]] for point in points]

# Add heatmap layer
HeatMap(heat_data, radius=15).add_to(map_warsaw)

# Save the map to an HTML file
map_warsaw.save("../warsaw_heatmap.html")