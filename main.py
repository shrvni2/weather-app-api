```python
import tkinter as tk
from tkinter import messagebox
import requests
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("300x200")
        self.city_label = tk.Label(root, text="City:")
        self.city_label.pack()
        self.city_entry = tk.Entry(root)
        self.city_entry.pack()
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()
        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            api_key = "YOUR_API_KEY"
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                self.weather_label.config(text=f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
            else:
                messagebox.showerror("Error", "Failed to retrieve weather data")
        else:
            messagebox.showerror("Error", "Please enter a city")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```