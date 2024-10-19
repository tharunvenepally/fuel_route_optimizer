import pandas as pd
from math import radians, sin, cos, sqrt, atan2

def load_fuel_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading fuel data: {e}")
        return None

def find_nearby_stops(df, lat, lon, max_distance=500):
    if 'distance' not in df.columns:
        df['distance'] = df.apply(lambda row: haversine(lat, lon, row['Latitude'], row['Longitude']), axis=1)
    
    return df[df['distance'] <= max_distance]

def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c