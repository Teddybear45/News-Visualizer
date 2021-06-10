from folium.plugins import FastMarkerCluster, MarkerCluster

from glob import glob
import numpy as np
import folium
import os
from folium import plugins
from folium.plugins import HeatMap

def map_plot_cluster_reg(folium_map, full_query_map):
    locations = []

    for loc in full_query_map.keys():
        if loc is not None:
            loc_split = loc.split(",")
            loc_split[0] = float(loc_split[0])
            loc_split[1] = float(loc_split[1])
            locations.append(tuple(loc_split))

    icons = [folium.Icon(icon="paper-plane", prefix="fa", color="purple") for _ in range(len(locations))]
    popups_frame = []
    popup_content = []
    for coord in full_query_map:
        ner_loc = "<span>Location: {}</span> <br>".format(full_query_map[coord][0])
        links_content = ""
        for link in full_query_map[coord][1]:
            links_content += "<a href = \"{0}\" target=\"_blank\">{0} ,</a> <br>".format(link)

        articles = links_content
        content = ner_loc + articles

        frame = folium.IFrame(content)
        frame_content_popup = folium.Popup(frame, min_width=350, max_width=450)

        popups_frame.append(frame_content_popup)

    # popups = [folium.Popup(content) for content in popup_content]

    cluster = MarkerCluster(locations=locations, icons=icons, popups=popups_frame)

    folium_map.add_child(cluster)

    folium_map.save("index.html")


def append_heat_map_layer(folium_map, query_map):
    data = []
    for key in query_map:
        if key is not None:
            coords = key.split(",")
            data_element = [float(coords[0]), float(coords[1]), 1 + len(query_map[key][1]) * 0.6]
            data.append(data_element)


    print(data)

    HeatMap(data).add_to(folium.FeatureGroup(name='Heat Map').add_to(folium_map))
    folium.LayerControl().add_to(folium_map)

    folium_map.save("index.html")

