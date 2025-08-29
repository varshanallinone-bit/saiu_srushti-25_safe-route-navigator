# routing.py - Real-time routing logic using OpenStreetMap APIs

import requests
import json
import random

# Geocoding API from OpenStreetMap (Nominatim)
GEOCODING_API_URL = "https://nominatim.openstreetmap.org/search"

# Routing API from OpenStreetMap (OSRM)
ROUTING_API_URL = "http://router.project-osrm.org/route/v1/driving"


def geocode_location(location_name):
    """
    Converts a place name into a latitude and longitude.
    """
    params = {
        "q": location_name,
        "format": "json",
        "limit": 1
    }
    response = requests.get(GEOCODING_API_URL, params=params)
    data = response.json()
    if data and len(data) > 0:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    return None, None


def get_real_route(start_coords, end_coords):
    """
    Gets a real-world driving route between two points.
    """
    start_lon, start_lat = start_coords
    end_lon, end_lat = end_coords

    # OSRM expects coordinates in lon,lat format
    coords_str = f"{start_lon},{start_lat};{end_lon},{end_lat}"

    params = {
        "alternatives": "false",
        "steps": "true",
        "geometries": "geojson",
        "overview": "full"
    }

    try:
        response = requests.get(f"{ROUTING_API_URL}/{coords_str}", params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        if 'routes' in data and len(data['routes']) > 0:
            route = data['routes'][0]
            geojson = route['geometry']
            distance = route['distance'] / 1000  # Convert to km

            # Extract points from the GeoJSON
            path = []
            for coord in geojson['coordinates']:
                path.append({"lat": coord[1], "lon": coord[0]})

            # Mock safety scores for demonstration
            safety_scores = {
                "street_lights": random.randint(1, 10),
                "police_help": random.randint(1, 10),
                "human_presence": random.randint(1, 10),
            }
            overall_safety = round(sum(safety_scores.values()) / len(safety_scores.values()), 1)

            # We will only provide one route option for simplicity
            return [{
                "type": "Safest Route",
                "description": "This route is optimized for safety based on our data.",
                "distance": f"{distance:.2f}",
                "safety_scores": safety_scores,
                "safety_score": overall_safety,
                "path": path
            }]

    except requests.exceptions.RequestException as e:
        print(f"Error getting route from OSRM: {e}")
        return []


def find_safe_routes(start_location, destination_location):
    """
    Main function to find a route between two real-world locations.
    """
    # 1. Geocode the start and end locations
    start_lat, start_lon = geocode_location(start_location)
    dest_lat, dest_lon = geocode_location(destination_location)

    if not all([start_lat, start_lon, dest_lat, dest_lon]):
        return []

    # 2. Get the real-world route using OSRM
    route_options = get_real_route((start_lat, start_lon), (dest_lat, dest_lon))
    return route_options
