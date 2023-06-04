import folium
import geopy
import time
from geopy.extra.rate_limiter import RateLimiter

from app.geolocator import geo_map
from app.map_render import map_plot_cluster_reg, append_heat_map_layer

import csv

if __name__ == '__main__':
    start_time = time.time()

    loc_collection = dict()
    # loc_collection = {'Bellevue High School': 20, 'Newport High School': 10}

    with open ('regs.csv', "r"):
        reader = csv.reader(open('regs.csv', "r"))
        for n, row in enumerate(reader):
            if n != 0:
                loc_collection[row[1]] = row[0]

    print(loc_collection)


    locator = geopy.geocoders.Nominatim(user_agent="HackPNWMapper")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    query_map = geo_map(loc_collection, geocode)

    print(query_map)



    dark_folium_map = folium.Map(location=[47.673988, -122.121513],
                                 zoom_start=10,
                                 tiles='CartoDBdark_matter')

    map_plot_cluster_reg(dark_folium_map, query_map)
    append_heat_map_layer(dark_folium_map, query_map)

    print("--- %s seconds ---" % (time.time() - start_time))
