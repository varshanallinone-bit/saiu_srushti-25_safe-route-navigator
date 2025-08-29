# safe_route_app/main.py
# This is the main entry point for the Flask application.

from flask import Flask, request, jsonify, send_from_directory
from routing import find_safe_routes
from sos import trigger_sos_alert
import random
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Mock user database for demonstration purposes
users = {
    "user1@example.com": {"password": "password123"},
}


# --- UI Routes to serve HTML files ---
@app.route('/')
def serve_login():
    """Serves the main login page."""
    return send_from_directory('.', 'login.html')


@app.route('/create-account')
def serve_create_account():
    """Serves the create account page."""
    return send_from_directory('.', 'create-account.html')


@app.route('/welcome')
def serve_welcome():
    """Serves the welcome page."""
    return send_from_directory('.', 'welcome.html')


@app.route('/dashboard')
def serve_dashboard():
    """Serves the dashboard page."""
    return send_from_directory('.', 'dashboard.html')


@app.route('/map')
def serve_map():
    """Serves the map and route selection page."""
    return send_from_directory('.', 'map.html')


# --- API Endpoints ---
@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in users and users[email]['password'] == password:
        return jsonify({"message": "Login successful", "redirect": "/welcome"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/register', methods=['POST'])
def register():
    """
    Handles new user registration. Mocks adding a new user.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if email in users:
        return jsonify({"error": "User with this email already exists"}), 409

    users[email] = {"password": password}
    return jsonify({"message": "Account created successfully", "redirect": "/"}), 201


@app.route('/routes', methods=['POST'])
def routes():
    """
    Provides route options with safety scores by calling the routing logic.
    """
    data = request.json
    start = data.get('start_location')
    destination = data.get('destination_location')

    if not start or not destination:
        return jsonify({"error": "Start and destination locations are required"}), 400

    # Call the function to find routes with safety scores
    route_options = find_safe_routes(start, destination)

    return jsonify({"routes": route_options}), 200


@app.route('/request_camera_otp', methods=['POST'])
def camera_otp():
    """
    Simulates requesting an OTP for camera access.
    """
    data = request.json
    camera_id = data.get('camera_id')

    otp = str(random.randint(1000, 9999))
    print(f"Generated OTP for camera {camera_id}: {otp}")

    return jsonify({"message": "OTP sent", "otp": otp}), 200


@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    """
    Verifies the OTP for camera access.
    """
    data = request.json
    user_otp = data.get('otp')
    if user_otp == "1234":  # Mock OTP for testing purposes
        return jsonify({"message": "OTP verified successfully", "access_granted": True}), 200
    else:
        return jsonify({"error": "Invalid OTP"}), 401


@app.route('/sos', methods=['POST'])
def sos():
    """
    Triggers an SOS alert to the police by calling the SOS logic.
    """
    data = request.json
    user_location = data.get('location')

    if not user_location:
        return jsonify({"error": "User location is required"}), 400

    alert_status = trigger_sos_alert(user_location)

    return jsonify({"status": alert_status}), 200


if __name__ == '__main__':
    app.run(debug=True)
