import requests
import matplotlib.pyplot as plt
from datetime import datetime
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"

def get_weather_data(lon, lat, api_key):
    """
    Fetches weather data from OpenWeatherMap API for the given coordinates.
    """
    url = f"{BASE_URL}lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    # print(response.json())
    return response.json()

# Function to convert Kelvin to Fahrenheit
def covert_to_fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

def analyze_weather_data(data):
    """
    Analyzes the weather data, calculates average temperature.
    """
    temps = [entry['main']['temp'] for entry in data['list']]
    last_5_days_temps = [covert_to_fahrenheit(temp) for temp in temps]
    print(last_5_days_temps)
    return sum(last_5_days_temps) / len(last_5_days_temps), last_5_days_temps

def plot_weather_trends(temps):
    """
    Plots the temperature trends on a line chart.
    """
    dates = [datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d') for day in data['list']]
    plt.plot(dates, temps, marker='o')
    plt.title('3-Hour/5-Day Weather Trend')
    plt.xlabel('Date')
    plt.ylabel('Day Temperature (°F)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lon = input("Enter the city's Latitude: ")
    lat = input("Enter the city's Longitude: ")
    data = get_weather_data(lon, lat, API_KEY)

    if data.get('list'):
        average_temp, temps = analyze_weather_data(data)
        print(f"The average temperature for the next 5 days at Coordinates {lon, lat} is: {average_temp:.2f}°C")
        plot_weather_trends(temps)
    else:
        print("Error fetching weather data.")
