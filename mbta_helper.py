import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pprint import pprint

# Your API KEYS (you need to use your own keys - very long random characters)
MAPBOX_TOKEN = "pk.eyJ1IjoibXN5MDExMDE1IiwiYSI6ImNsZnpxZjFneTB3aGwzb3Bhb3RubGRvZ28ifQ.zFSapXqQ8ccVtVLWG4qIVA"


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# A little bit of scaffolding if you want to use it

def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    replacement = "%20"
    output_place = place_name.replace(" ", replacement)
    query = output_place
    url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    lat_long = tuple(response_data['features'][0]['geometry']['coordinates'])
    lat_long = tuple(f"{coord:.4f}" for coord in lat_long)
    lat_long = tuple(reversed(lat_long))
    # print(type(lat_long))
    return lat_long
        
def get_transportation_means() -> str:
    """
    Prompts the user to enter their preferred transportation means and returns it as a string.
    """
    while True:
        transportation_means = input("Enter your preferred transportation means (Bus, Subway, or Commuter Rail): ")
        if transportation_means.lower() not in ['bus', 'subway', 'commuter rail']:
            print("Invalid transportation means. Please enter Bus, Subway, or Commuter Rail.")
        else:
            return transportation_means.lower()


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    
    MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        if len(response_data['data']) == 0:
            return None
        station_name = response_data['data'][0]['attributes']['name']
        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding'] == 1
        return (station_name, wheelchair_accessible)


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address after select the transportation means you want, return the nearest MBTA stop and whether it is wheelchair accessible.
    

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    transportation_type = get_transportation_means()

    if not transportation_type:
        print("Invalid transportation means.")

    transportation_type_mapping = {
        1 : "Subway",
        2 : "Commuter Rail",
        3 : "Bus"
    }

    if not transportation_type:
        print("Invalid transportation means.")
        return None

    MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        stops = response_data['data']
    filtered_stops = [stop for stop in stops if stop['attributes']['vehicle_type'] in transportation_type_mapping.keys() and transportation_type_mapping[stop['attributes']['vehicle_type']] == transportation_type]
    if len(filtered_stops) == 0:
        print(f"No {transportation_type} stops found near {place_name}.")
        return None
    station_name = filtered_stops[0]['attributes']['name']
    wheelchair_accessible = filtered_stops[0]['attributes']['wheelchair_boarding'] == 1
    return (station_name, wheelchair_accessible)

def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long("Babson College"))
    # print(get_lat_long("boston university"))
    # print(get_nearest_station("42.350692" ,"-71.1063435"))
    print(find_stop_near('brandeis university'))
    
if __name__ == '__main__':
    main()
