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
query = "Babson%20College"
url = f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
# print(url)

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)


MBTA_API_KEY = "fb950d9d0aaa490aac903e818b264994"
url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={52.3702308418161662}&filter%5Blongitude%5D={4.896977862308262}"
with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint (response_data)