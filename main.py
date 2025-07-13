from flask import Flask, render_template, request, flash
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate random secret key

# Get API key from environment
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable is required")


@app.route("/", methods=["GET", "POST"])
def get_weather():
    if request.method == "POST":
        city = request.form["city"].strip()
        if not city:
            flash("Please enter a city name", "error")
            city = "Waterloo"
    else:
        city = "Waterloo"

    # Construct URL using environment variable
    construct_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"

    try:
        response = requests.get(construct_url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        list_of_data = response.json()
        
        # Check if the API returned an error
        if list_of_data.get('cod') != 200:
            flash(f"Error: {list_of_data.get('message', 'Unknown error')}", "error")
            return render_template('weather.html', data=None)
        
        # print(list_of_data)  # For debugging

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
            "temp_cel": f"{round(list_of_data['main']['temp'] - 273.15)}°C",
            "pressure": f"{list_of_data['main']['pressure']} hPa",
            "humidity": f"{list_of_data['main']['humidity']}%",
            "wind_speed": f"{round(list_of_data['wind']['speed'] * 3.6)} km/h",
            "cityname": city.title()
        }
        return render_template('weather.html', data=data)
    
    except requests.exceptions.RequestException as e:
        flash(f"Error fetching weather data: {str(e)}", "error")
        return render_template('weather.html', data=None)
    except KeyError as e:
        flash(f"Error parsing weather data: Missing field {str(e)}", "error")
        return render_template('weather.html', data=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')

# For Vercel deployment
app = app
