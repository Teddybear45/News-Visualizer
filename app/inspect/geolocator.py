import time

import pandas as pd
import geopy
import matplotlib.pyplot as plt
from geopy.extra.rate_limiter import RateLimiter


def geo_map(loc_article_map, geocode_element):
    geo_loc_article_map = {}

    keys = loc_article_map.keys()
    df = pd.DataFrame({"name_token": keys})

    df['location'] = df['name_token'].apply(geocode_element)

    df['point'] = df['location'].apply(lambda location: str(location.latitude) + "," + str(location.longitude) if location else None)

    for name, loc in zip(df.get('name_token'), df.get('point')):
        geo_loc_article_map[loc] = (name, loc_article_map[name])

    print(df)

    return geo_loc_article_map









