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

## Environment Variables

- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key (required)
- `FLASK_ENV`: Flask environment (development/production)
- `FLASK_DEBUG`: Enable/disable debug mode (True/False)
- `SECRET_KEY`: Flask secret key for session management

## API Reference

This app uses the OpenWeatherMap Current Weather API:
- API Documentation: https://openweathermap.org/current
- Get your free API key: https://openweathermap.org/api

## Deployment

### Vercel Deployment (Recommended)

1. **Fork/Clone this repository**

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com) and sign in with GitHub
   - Click "New Project" and import your repository
   - Vercel will automatically detect it's a Python project

3. **Set Environment Variables:**
   - In Vercel dashboard, go to your project settings
   - Add environment variable: `OPENWEATHER_API_KEY` with your API key value
   - Deploy!

4. **Domain:** Your app will be available at `https://your-project-name.vercel.app`

### Other Deployment Options

#### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
heroku config:set OPENWEATHER_API_KEY=your_api_key_here
git push heroku main
```

#### Railway
```bash
# Install Railway CLI, then:
railway login
railway new
railway add
railway deploy
```

#### Local Development
```bash
python run.py
# Visit http://localhost:5000
```

### Production Considerations

- **Environment Variables:** Always set `OPENWEATHER_API_KEY` in your deployment platform
- **HTTPS:** Most platforms (Vercel, Heroku, Railway) provide HTTPS automatically
- **Monitoring:** Consider adding application monitoring in production
- **Rate Limiting:** OpenWeatherMap free tier has rate limits (60 calls/minute)

## Security Notes

- Never commit your `.env` file to version control
- Use strong, random secret keys in production
- Consider implementing rate limiting for API calls
- Use HTTPS in production

## License

This project is open source and available under the MIT License.
