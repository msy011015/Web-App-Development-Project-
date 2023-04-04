import urllib.request
import json
import ssl
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPBOX_TOKEN = "pk.eyJ1IjoibXN5MDExMDE1IiwiYSI6ImNsZnpxZjFneTB3aGwzb3Bhb3RubGRvZ28ifQ.zFSapXqQ8ccVtVLWG4qIVA"
MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
query = "Babson%20College"
url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url)

def get_location(address):
    """
    get location information
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={MAPBOX_TOKEN}&types=poi"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data

def get_mbta_location(latitude, longtitude):
    """
    Find nearby stations using latitude and longtitude
    """
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longtitude}"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data


if __name__ == "__main__":
    query = "Boston%20University"
    location_data = get_location(query)
    # pprint (location_data)
    latitude,longtitude = location_data ["features"][0]["center"]
    mbta_station = get_mbta_location (latitude,longtitude)
    pprint(mbta_station)


# query = "Babson College"
# types = "poi"

# params = {"access_token": MAPBOX_TOKEN,"types": types}
# query_string = urllib.parse.urlencode (params)

# url = f"{https://api.mapbox.com/geocoding/v5/mapbox.places}/{query}.json?{query_string}"