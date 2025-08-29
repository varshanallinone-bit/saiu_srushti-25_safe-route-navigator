# Safe Route Navigator
APPLICATION OVERVIEW:

Safe Route Navigator is a web application designed to help users find the safest routes to their destinations. It provides a user-friendly interface to search for routes, and it incorporates a backend system that can provide safety scores and trigger SOS alerts for emergencies.

FEATURES:

User Authentication: Secure login and account creation pages for managing user access.

Interactive Map: An integrated map powered by Leaflet.js to visualize routes.

Safety-Optimized Routing: The application uses OpenStreetMap (OSRM) to calculate routes and provides a safety score based on a simulated set of criteria.

Emergency SOS Alert: A one-click SOS button to send an immediate alert to a simulated police station, providing peace of mind during travel.

Mock Live Street View: A demo feature to simulate a live camera feed, accessible via a mock OTP for a realistic feel.

TECHNOLOGIES USED:

This project is a full-stack application built with the following technologies:

FRONTEND

HTML: For the structure of all web pages.

CSS: Styled using Tailwind CSS for a modern, responsive design.

JavaScript: For all interactive functionality, including form handling and API calls.

Leaflet.js: An open-source JavaScript library for interactive maps.

BACKEND

Python: The core logic of the application.

Flask: A micro-web framework for handling API endpoints and serving HTML files.

Flask-CORS: To handle cross-origin requests between the frontend and backend.

Requests: A Python library for making HTTP requests to external APIs.

# Getting Started

Prerequisites

Python 3.x

Pip (Python package installer)

Installation

Clone the repository:

git clone [https://github.com/your-username/safe-route-navigator.git](https://github.com/your-username/safe-route-navigator.git)

Navigate to the project directory:

cd safe-route-navigator

Install the required Python packages:

pip install Flask Flask-Cors requests

Usage

Start the Flask server from the terminal:

python main.py

Open your web browser and navigate to http://127.0.0.1:5000/.

Application Developed by: 

T. SRIVARSHAN (Coordinator and UX Developer)

BD THOUFIQ AHMED (Frontend Developer)

SRINATH D (Assistant Developer)

License
This project is licensed under the MIT License.
