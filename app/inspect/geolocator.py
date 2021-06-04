import time

import pandas as pd
import geopy
import matplotlib.pyplot as plt
from geopy.extra.rate_limiter import RateLimiter







if __name__ == '__main__':
    start_time = time.time()

    locator = geopy.geocoders.Nominatim(user_agent="NewsMapper")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    keys = ["Tokyo", "Seattle", "Washington", "Ota City"]

    df = pd.DataFrame({"name_token": keys})

    df['location'] = df['name_token'].apply(geocode)

    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

    print(df)
    print(time.time() - start_time)


