import logging

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from rtree import index


class DataAnalyzer:
    def __init__(self, bus_data_list):
        self.bus_data_list = bus_data_list

    def buses_exceeding_50(self):
        df = pd.DataFrame(self.bus_data_list)

        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

        # Drop rows with NaT (missing or invalid datetime)
        df = df.dropna(subset=['Time'])

        df.sort_values(by=['VehicleNumber', 'Time'], inplace=True)

        df['distance'] = np.hstack(df.groupby('VehicleNumber')
                                   .apply(lambda x: DataAnalyzer.haversine(x['Lat'], x['Lon'],
                                                                           x['Lat'].shift(), x['Lon'].shift())).values)

        # Calculate time difference between consecutive points (in hours)
        df['time_diff'] = df.groupby('VehicleNumber')['Time'].diff().dt.total_seconds() / 3600

        # Calculate speed (in km/h)
        df['speed'] = df['distance'] / df['time_diff']

        df = df[df['speed'].notna()]

        rows, column = df.shape

        # Remove unrealistic values
        df = df[(df['speed'] <= 90)]

        rows_filtered, columns_filtered = df.shape
        logging.warn(f"Removed unrealistic data ({((rows - rows_filtered) / rows_filtered) * 100}%)")

        df_exceeded = df[df['speed'] > 50]

        return df_exceeded["VehicleNumber"].nunique(), DataAnalyzer.high_percentage_points(df, df_exceeded, 0.001)

    @staticmethod
    def points_in_radius(lat, lon, all_points, exceeded_points, radius):
        all_points_count = all_points.apply(
            lambda row: DataAnalyzer.haversine(lat, lon, row['Lat'], row['Lon']) > radius, axis=1).sum()
        exceeded_points_points_count = exceeded_points.apply(
            lambda row: DataAnalyzer.haversine(lat, lon, row['Lat'], row['Lon']) > radius, axis=1).sum()

        return exceeded_points_points_count / all_points_count

    @staticmethod
    def high_percentage_points(all_points, exceeded_points, radius):
        res = []

        p_index_all = index.Index()
        p_index_exceeded = index.Index()

        for idx, row in all_points.iterrows():
            lat = row['Lat']
            lon = row['Lon']
            p_index_all.insert(idx, (lon, lat, lon, lat))

        for idx, row in exceeded_points.iterrows():
            lat = row['Lat']
            lon = row['Lon']
            p_index_exceeded.insert(idx, (lon, lat, lon, lat))

        counter = 0

        for idx, row in all_points.iterrows():
            logging.warn(f"{counter}")
            counter += 1
            lat = row['Lat']
            lon = row['Lon']

            neighbors_all = list(p_index_all.intersection((lon - radius, lat - radius, lon + radius, lat + radius)))
            neighbors_exceeded = list(
                p_index_exceeded.intersection((lon - radius, lat - radius, lon + radius, lat + radius)))

            # logging.warn(f"Percentage: {len(neighbors_exceeded) / len(neighbors_all)}")

            if len(neighbors_exceeded) / len(neighbors_all) > 0.5:
                res.append((lat, lon))

        logging.warn(f"{len(res)},{len(exceeded_points)}")
        # return list(zip(exceeded_points['Lat'], exceeded_points['Lon']))
        return res

    # Calculate distance between consecutive points (in km)
    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        from numpy import radians, sin, cos, sqrt, arctan2
        # Convert coordinates from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * arctan2(sqrt(a), sqrt(1 - a))
        # Radius of the Earth in km
        R = 6371
        return R * c