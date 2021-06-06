import folium
from folium.plugins import FastMarkerCluster


if __name__ == '__main__':
    highest_location = [45.5236, -122.6750]

    m = folium.Map(location=highest_location, zoom_start=12, tiles="OpenStreetMap")
    folium.Marker(
        [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip="tooltip123"
    ).add_to(m)


    m.save("index.html")






