#!/usr/bin/env python3
"""
Simple script to run the weather app with proper configuration.
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if required environment variables are set
if not os.getenv('OPENWEATHER_API_KEY'):
    print("Error: OPENWEATHER_API_KEY environment variable is not set!")
    sys.exit(1)

# Import and run the app
from main import app

if __name__ == '__main__':
    print("Starting Weather App...")
    print("Visit http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=True)
