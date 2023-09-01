# # Amali Backend
This  backend serves as the central storage and management system for data to be used by our  mobile application. It provides the necessary APIs and functionality to store, retrieve, and manipulate data to support the mobile application's features and user interactions.
## Installation
# 1. Clone the repository:
  git clone https://github.com/akirachix/Amali-backend
# Cd In To The Repository
cd Amali-Backend
# Create a virtual environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install required packages:
pip install -r requirements.txt
# Set up the database:
python3 manage.py migrate
# Create a superuser (admin) account
python3 manage.py createsuperuser
# Start the development server
python3 manage.py runserver
# Access App
Access the app at http://127.0.0.1:8000/.







