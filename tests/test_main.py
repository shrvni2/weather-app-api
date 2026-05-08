```python
import pytest
from unittest.mock import patch, MagicMock
from main import WeatherApp
from api_integration import APIIntegration
import tkinter as tk
from tkinter import messagebox
import requests
import json

def test_weather_app_init():
    root = tk.Tk()
    app = WeatherApp(root)
    assert app.root == root
    assert app.city_label.cget("text") == "City:"
    assert app.get_weather_button.cget("text") == "Get Weather"

def test_get_weather_normal_case():
    root = tk.Tk()
    app = WeatherApp(root)
    app.city_entry.insert(0, "London")
    with patch("main.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [{"description": "sunny"}],
            "main": {"temp": 20, "humidity": 60},
            "name": "London"
        }
        mock_get.return_value = mock_response
        app.get_weather()
        assert app.weather_label.cget("text") == "Weather: sunny\nTemperature: 20.0°C\nHumidity: 60%"

def test_get_weather_error_case():
    root = tk.Tk()
    app = WeatherApp(root)
    app.city_entry.insert(0, "London")
    with patch("main.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        with patch("main.messagebox.showerror") as mock_showerror:
            app.get_weather()
            mock_showerror.assert_called_once_with("Error", "Failed to retrieve weather data")

def test_get_weather_empty_city():
    root = tk.Tk()
    app = WeatherApp(root)
    with patch("main.messagebox.showerror") as mock_showerror:
        app.get_weather()
        mock_showerror.assert_called_once_with("Error", "Please enter a city")

def test_api_integration_init():
    api_key = "YOUR_API_KEY"
    api_integration = APIIntegration(api_key)
    assert api_integration.api_key == api_key
    assert api_integration.base_url == "http://api.openweathermap.org/data/2.5/weather"

def test_api_integration_get_weather_normal_case():
    api_key = "YOUR_API_KEY"
    api_integration = APIIntegration(api_key)
    with patch("api_integration.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [{"description": "sunny"}],
            "main": {"temp": 20, "humidity": 60},
            "name": "London"
        }
        mock_get.return_value = mock_response
        weather_data = api_integration.get_weather("London")
        assert weather_data == mock_response.json.return_value

def test_api_integration_get_weather_error_case():
    api_key = "YOUR_API_KEY"
    api_integration = APIIntegration(api_key)
    with patch("api_integration.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        weather_data = api_integration.get_weather("London")
        assert weather_data is None

def test_api_integration_parse_weather_data_normal_case():
    api_key = "YOUR_API_KEY"
    api_integration = APIIntegration(api_key)
    weather_data = {
        "weather": [{"description": "sunny"}],
        "main": {"temp": 20, "humidity": 60},
        "name": "London"
    }
    parsed_weather_data = api_integration.parse_weather_data(weather_data)
    assert parsed_weather_data == {
        "temperature": 20,
        "humidity": 60,
        "description": "sunny",
        "city": "London"
    }

def test_api_integration_parse_weather_data_error_case():
    api_key = "YOUR_API_KEY"
    api_integration = APIIntegration(api_key)
    weather_data = None
    parsed_weather_data = api_integration.parse_weather_data(weather_data)
    assert parsed_weather_data is None
```