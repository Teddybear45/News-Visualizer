import pandas as pd


# Define the custom function to filter results by state
def filter_by_state(location, state):
    if location is not None and location.raw['address'].get('state') == state:
        return location
    else:
        return None

# returns map of location names to coordinates. takes location names and articles map
def geo_map(loc_article_map, geocode_element):
    geo_loc_article_map = {}

    keys = loc_article_map.keys()
    df = pd.DataFrame({"name_token": keys})

    df['location'] = df['name_token'].apply(geocode_element)

    df['point'] = df['location'].apply(
        lambda location: str(location.latitude) + "," + str(location.longitude) if location else None)

    # Filter the results based on a specific state
    desired_state = 'Washington'  # Replace with the state you want to fence to
    df['location'] = df['location'].apply(filter_by_state, state=desired_state)

    for name, loc in zip(df.get('name_token'), df.get('point')):
        geo_loc_article_map[loc] = (name, loc_article_map[name])

    return geo_loc_article_map
