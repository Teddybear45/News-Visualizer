import folium
import geopy
import stanza
import time
from geopy.extra.rate_limiter import RateLimiter

from app.inspect.analyzer import parse_paper, process_paper
from app.inspect.geolocator import geo_map
from app.render.map_render import map_plot_cluster_reg, append_heat_map_layer
from app.source.collector import collect, get_config

import csv

if __name__ == '__main__':
    start_time = time.time()
    article_list = collect()
    print(article_list)
    stanza.download('en')
    nlp_pipline = stanza.Pipeline(lang='en', processors='tokenize,ner')

    loc_collection = dict()
    for article in article_list:
        article_txt = parse_paper(article)
        locations = process_paper(article_txt, nlp_pipline)
        for loc in locations:
            if loc in loc_collection:
                loc_collection[loc].append(article.url)
            else:
                loc_collection[loc] = [article.url]

    print(loc_collection)

    locator = geopy.geocoders.Nominatim(user_agent="NewsMapper")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    query_map = geo_map(loc_collection, geocode)

    try:
        query_map.pop(None)
    except:
        print("-- All recognized --")

    print(query_map)


    with open("current_vals.csv", "w") as outfile:
        writer = csv.writer(outfile)
        for key, val in query_map.items():
            writer.writerow([key, val])

    dark_folium_map = folium.Map(location=[59.338315, 18.089960],
                                 zoom_start=3,
                                 tiles='CartoDBdark_matter')

    map_plot_cluster_reg(dark_folium_map, query_map)
    append_heat_map_layer(dark_folium_map, query_map)

    print("--- %s seconds ---" % (time.time() - start_time))


