# safe_route_app/sos.py
# This module handles the SOS alert functionality.
import json
import random


def get_nearest_police_station(location):
    """
    Finds the nearest police station to a given location.
    This is a mock implementation. A real app would use a geo-spatial database
    or a dedicated API to find the closest emergency service provider.
    """
    # Mock list of police stations
    stations = [
        {"id": "PS1", "name": "Main City Police Station", "location": "123 Oak St"},
        {"id": "PS2", "name": "Downtown Patrol Station", "location": "456 Pine Ave"},
        {"id": "PS3", "name": "Suburban Precinct", "location": "789 Elm Blvd"}
    ]

    # Just return a random station for now for demonstration purposes
    return random.choice(stations)


def trigger_sos_alert(user_location):
    """
    Simulates triggering an SOS alert.
    Sends user location and a simulated alert to the nearest police station.
    """
    try:
        # Find the nearest police station based on the user's location
        station = get_nearest_police_station(user_location)

        # In a real system, this is where the alert would be sent
        # to a police dispatch system via an API or other communication method.
        print(f"SOS alert triggered at location: {user_location}")
        print(f"Alert sent to nearest police station: {station['name']} ({station['location']})")
        print("A call is being initiated to the user's registered phone number.")

        # Return a success message
        return "SOS alert successfully sent to police and support teams."
    except Exception as e:
        # Handle any potential errors during the process
        print(f"Error triggering SOS alert: {e}")
        return "Failed to trigger SOS alert. Please try again."

