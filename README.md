# Weather App

A simple Flask-based weather application that fetches weather data from OpenWeatherMap API.

## Features

- Search weather by city name
- Display temperature, humidity, pressure, wind speed, and coordinates
- Error handling for invalid cities and API failures
- Responsive Bootstrap UI
- Environment variable configuration for security

## Setup Instructions

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- OpenWeatherMap API key (free at https://openweathermap.org/api)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rickytang666/rt-weather-app.git
   cd rt-weather-app
   ```

2. **Install dependencies:**
   ```bash
   # Modern way (recommended)
   pip install -e .
   
   # Or traditional way
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file
   echo "OPENWEATHER_API_KEY=your_actual_api_key_here" > .env
   ```

4. **Get your API key:**
   - Go to [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key from the dashboard
   - Replace `your_actual_api_key_here` in the .env file

### Running the Application

#### Development mode:
```bash
python run.py
```

#### Or run directly:
```bash
python main.py
```

#### Production mode (using Gunicorn):
```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

The application will be available at `http://localhost:5000`

## API Reference

This app uses the OpenWeatherMap Current Weather API:
- API Documentation: https://openweathermap.org/current
- Get your free API key: https://openweathermap.org/api