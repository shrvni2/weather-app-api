```python
# config.py

class Config:
    def __init__(self):
        self.api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.units = "metric"

    def get_api_key(self):
        return self.api_key

    def get_base_url(self):
        return self.base_url

    def get_units(self):
        return self.units

config = Config()
```