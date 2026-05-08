```python
import json
from api_integration import APIIntegration

class WeatherData:
    def __init__(self, api_key):
        self.api_integration = APIIntegration(api_key)
        self.weather_data = {}

    def fetch_weather(self, city):
        weather_response = self.api_integration.get_weather(city)
        if weather_response:
            self.weather_data[city] = weather_response
            return weather_response
        else:
            return None

    def get_weather(self, city):
        if city in self.weather_data:
            return self.weather_data[city]
        else:
            return self.fetch_weather(city)

    def save_weather_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.weather_data, file)

    def load_weather_data(self, filename):
        try:
            with open(filename, 'r') as file:
                self.weather_data = json.load(file)
        except FileNotFoundError:
            pass

    def get_temperature(self, city):
        weather = self.get_weather(city)
        if weather:
            return weather['main']['temp']
        else:
            return None

    def get_description(self, city):
        weather = self.get_weather(city)
        if weather:
            return weather['weather'][0]['description']
        else:
            return None

    def get_humidity(self, city):
        weather = self.get_weather(city)
        if weather:
            return weather['main']['humidity']
        else:
            return None

    def get_wind_speed(self, city):
        weather = self.get_weather(city)
        if weather:
            return weather['wind']['speed']
        else:
            return None
```