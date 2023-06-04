from folium.plugins import MarkerCluster

import folium
from folium.plugins import HeatMap


# maps and saves to index.html cluster items given coord, location, article map. markers include popup
def map_plot_cluster_reg(folium_map, full_query_map):
    locations = []

    for loc in full_query_map.keys():
        if loc is not None:
            loc_split = loc.split(",")
            loc_split[0] = float(loc_split[0])
            loc_split[1] = float(loc_split[1])
            locations.append(tuple(loc_split))

    icons = [folium.Icon(icon="paper-plane", prefix="fa", color="purple") for _ in range(len(locations))]
    popups_frames = []
    for coord in full_query_map:
        ner_loc = "<span>Location: {}</span> <br>".format(full_query_map[coord][0])


        frame = folium.IFrame(ner_loc)
        frame_content_popup = folium.Popup(frame, min_width=350, max_width=450)

        popups_frames.append(frame_content_popup)

    cluster = MarkerCluster(locations=locations, icons=icons, popups=popups_frames)

    folium_map.add_child(cluster)

    folium_map.save("index.html")


# adds heat map layer to cluster or regular map
def append_heat_map_layer(folium_map, query_map):
    data = []
    for key in query_map:
        if key is not None:
            coords = key.split(",")
            data_element = [float(coords[0]), float(coords[1]), int(query_map[key][1])]
            data.append(data_element)

    HeatMap(data).add_to(folium.FeatureGroup(name='Heat Map').add_to(folium_map))
    folium.LayerControl().add_to(folium_map)

    folium_map.save("index.html")
