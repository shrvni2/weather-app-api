# 🌞 Weather App API
A simple weather app using Python and API integration.

## 📝 Description
The weather-app-api project is a basic implementation of a weather application that retrieves and displays the current weather for a given city. The application utilizes the OpenWeatherMap API to fetch weather data and is built using Python.

## 🌈 Features
* Retrieves current weather data for a specified city
* Displays weather information in a simple GUI
* Handles API requests and responses
* Includes basic error handling for invalid city names or API errors

## 🛠️ Tech Stack
* Python 3.x
* Tkinter for GUI
* Requests for API integration
* OpenWeatherMap API for weather data

## 📦 Installation
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key in the `config.py` file.

## 🚀 Usage
To run the application, execute the `main.py` file:
```bash
python main.py
```
Enter a city name in the input field and click the "Get Weather" button to retrieve and display the current weather.

## 🗂️ Project Structure
* `main.py`: The main application file
* `api_integration.py`: Handles API requests and responses
* `weather_data.py`: Processes and stores weather data
* `config.py`: Stores configuration settings, including the API key
* `tests/test_main.py`: Unit tests for the main application
* `requirements.txt`: Lists dependencies required by the project
* `.gitignore`: Specifies files and directories to ignore in the Git repository

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
https://github.com/shrvni2/weather-app-api