import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# OpenWeatherMap API key
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather_data(destination, start_date, end_date):
    """
    Fetch weather data for the destination and dates
    
    Args:
        destination (str): City name or coordinates
        start_date (str): Start date in format 'YYYY-MM-DD'
        end_date (str): End date in format 'YYYY-MM-DD'
    
    Returns:
        dict: Weather data including temperature, conditions, and recommendations
    """
    try:
        # Get coordinates for destination
        coords = get_coordinates(destination)
        if not coords:
            return None
        
        # Fetch weather forecast
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        
        weather_data = response.json()
        
        # Process and aggregate weather data
        return process_weather_data(weather_data, start_date, end_date)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        # Return mock data for demonstration
        return get_mock_weather_data(destination)

def get_coordinates(destination):
    """
    Get latitude and longitude for a destination
    
    Args:
        destination (str): City name
    
    Returns:
        dict: Coordinates with 'lat' and 'lon' keys
    """
    try:
        geo_url = 'https://nominatim.openstreetmap.org/search'
        params = {'q': destination, 'format': 'json'}
        
        response = requests.get(geo_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if data:
            return {
                'lat': float(data[0]['lat']),
                'lon': float(data[0]['lon'])
            }
        return None
    
    except Exception as e:
        print(f"Error getting coordinates: {e}")
        return None

def process_weather_data(weather_data, start_date, end_date):
    """
    Process raw weather data into useful information
    
    Args:
        weather_data (dict): Raw API response
        start_date (str): Start date in format 'YYYY-MM-DD'
        end_date (str): End date in format 'YYYY-MM-DD'
    
    Returns:
        dict: Processed weather data
    """
    try:
        forecasts = weather_data.get('list', [])
        
        temperatures = []
        conditions = {}
        precipitation_chance = 0
        wind_speed = []
        humidity = []
        
        for forecast in forecasts:
            dt = datetime.fromtimestamp(forecast['dt'])
            date_str = dt.strftime('%Y-%m-%d')
            
            # Check if forecast is within date range
            if start_date <= date_str <= end_date:
                temperatures.append(forecast['main']['temp'])
                wind_speed.append(forecast['wind']['speed'])
                humidity.append(forecast['main']['humidity'])
                
                condition = forecast['weather'][0]['main']
                conditions[condition] = conditions.get(condition, 0) + 1
                
                if 'rain' in forecast:
                    precipitation_chance = max(precipitation_chance, forecast.get('pop', 0) * 100)
        
        if not temperatures:
            return get_mock_weather_data()
        
        # Calculate averages
        avg_temp = sum(temperatures) / len(temperatures)
        avg_humidity = sum(humidity) / len(humidity)
        avg_wind = sum(wind_speed) / len(wind_speed)
        
        # Find most common condition
        primary_condition = max(conditions, key=conditions.get) if conditions else 'Sunny'
        
        return {
            'destination': weather_data.get('city', {}).get('name', 'Unknown'),
            'avg_temperature': round(avg_temp, 1),
            'min_temperature': round(min(temperatures), 1),
            'max_temperature': round(max(temperatures), 1),
            'condition': primary_condition,
            'humidity': round(avg_humidity, 1),
            'wind_speed': round(avg_wind, 1),
            'precipitation_chance': round(precipitation_chance, 1),
            'all_conditions': dict(conditions)
        }
    
    except Exception as e:
        print(f"Error processing weather data: {e}")
        return get_mock_weather_data()

def get_mock_weather_data(destination='Unknown'):
    """
    Return mock weather data for demonstration
    
    Args:
        destination (str): Destination city
    
    Returns:
        dict: Mock weather data
    """
    return {
        'destination': destination,
        'avg_temperature': 22.5,
        'min_temperature': 18.0,
        'max_temperature': 28.0,
        'condition': 'Partly Cloudy',
        'humidity': 65.0,
        'wind_speed': 12.5,
        'precipitation_chance': 20.0,
        'all_conditions': {'Partly Cloudy': 3, 'Sunny': 2}
    }
