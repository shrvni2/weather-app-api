```python
import requests
import json

class APIIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def parse_weather_data(self, weather_data):
        if weather_data is not None:
            main_data = weather_data["main"]
            weather = weather_data["weather"][0]
            return {
                "temperature": main_data["temp"],
                "humidity": main_data["humidity"],
                "description": weather["description"],
                "city": weather_data["name"]
            }
        else:
            return None

def main():
    api_key = "YOUR_API_KEY_HERE"
    api_integration = APIIntegration(api_key)
    city = "London"
    weather_data = api_integration.get_weather(city)
    parsed_weather_data = api_integration.parse_weather_data(weather_data)
    print(parsed_weather_data)

if __name__ == "__main__":
    main()
```