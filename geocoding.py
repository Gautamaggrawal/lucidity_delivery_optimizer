import requests
from typing import Tuple
from config import NOMINATIM_SEARCH_URL, HEADERS

def get_coordinates(address: str) -> Tuple[float, float]:
    """Get coordinates for a location using Nominatim API."""
    params = {
        "q": address,
        "format": "json",
        "addressdetails": 1,
        "limit": 1,
    }

    response = requests.get(NOMINATIM_SEARCH_URL, params=params, headers=HEADERS)
    
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        lat = float(data["lat"])
        lon = float(data["lon"])
        print(f"Debug: Extracted Coordinates for {address}: Latitude: {lat}, Longitude: {lon}")
        return lat, lon
    else:
        print(f"Could not fetch coordinates for address: {address}")
        return manual_coordinate_input(address)

def manual_coordinate_input(location_name: str) -> Tuple[float, float]:
    """Allow manual input of coordinates if geocoding fails."""
    print(f"\nPlease enter coordinates for {location_name}:")
    while True:
        try:
            lat = float(input("Enter latitude (e.g., 12.9279): "))
            lng = float(input("Enter longitude (e.g., 77.6271): "))
            if -90 <= lat <= 90 and -180 <= lng <= 180:
                return lat, lng
            else:
                print("Invalid coordinates! Please try again.")
        except ValueError:
            print("Please enter valid numbers!")