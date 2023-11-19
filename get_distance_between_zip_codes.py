import requests
import geopy.distance

def get_distance_between_zip_codes(zip_code1, zip_code2, country='us'):
    base_url = "https://nominatim.openstreetmap.org/search"


    zip_code1_params = {
        'format': 'json',
        'postalcode': zip_code1,
        'country': country, 
        'limit': 1
    }

    zip_code2_params = {
        'format': 'json',
        'postalcode': zip_code2,
        'country': country,
        'limit': 1
    }

    # Make requests to get zip code data
    zip_code1_response = requests.get(base_url, params=zip_code1_params)
    zip_code2_response = requests.get(base_url, params=zip_code2_params)

    # Get json data for zip codes 
    zip_code1_data = zip_code1_response.json()[0]
    zip_code2_data = zip_code2_response.json()[0]

    # Get latitude and longitude of zip codes
    zip_code1_coords = (float(zip_code1_data['lat']), float(zip_code1_data['lon'])) 
    zip_code2_coords = (float(zip_code2_data['lat']), float(zip_code2_data['lon']))

    # Get distance between zip codes in kilometers
    distance_km = geopy.distance.geodesic(zip_code1_coords, zip_code2_coords).km 

    # Convert distance to miles 
    distance_mi = 0.621371 * distance_km 
    print (f"{zip_code1} and {zip_code2} are {distance_mi:.3f} miles apart.")
    return distance_mi
