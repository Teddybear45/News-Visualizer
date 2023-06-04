import pandas as pd


# returns map of location names to coordinates. takes location names and articles map
def geo_map(loc_article_map, geocode_element):
    geo_loc_article_map = {}

    keys = loc_article_map.keys()
    df = pd.DataFrame({"name_token": keys})

    df['location'] = df['name_token'].apply(geocode_element)

    df['point'] = df['location'].apply(
        lambda location: str(location.latitude) + "," + str(location.longitude) if location else None)

    for name, loc in zip(df.get('name_token'), df.get('point')):
        geo_loc_article_map[loc] = (name, loc_article_map[name])

    return geo_loc_article_map
