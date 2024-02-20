import logging

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

        rows, column = df.shape

        # Remove unrealistic values
        df = df[(df['speed'] <= 90) | df['speed'].isna()]

        rows_filtered, columns_filtered = df.shape
        logging.warn(f"Removed unrealistic data ({((rows - rows_filtered) / rows_filtered) * 100}%)")

        df_exceeded = df[df['speed'] > 50]

        return df_exceeded["VehicleNumber"].nunique(), list(zip(df_exceeded['Lat'], df_exceeded['Lon']))

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