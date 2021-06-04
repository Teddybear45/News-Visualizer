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



if __name__ == '__main__':
    locator = geopy.geocoders.Nominatim(user_agent="NewsMapper")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    test_dict = {
        "Florida": ["url.something.com, another.com"],
        "Seattle": ["some.other.seattle.com, cool.source.org"]
    }

    print(geo_map(test_dict, geocode))





