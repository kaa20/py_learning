import pprint
import requests
from dateutil.parser import parse

class OpenWeatherMap:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]

        appid = 'get_your_appid_in_the_openweathermap'
        s_city = city + ',RU'
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
            params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        print("sending HTTP request")
        data = res.json()
        forecast = []
        for day_data in data['list']:
            forecast.append({
                "date": parse(day_data['dt_txt']),
                "temp_max": '{0:+3.0f}'.format(day_data['main']['temp_max']),
                "description": day_data['weather'][0]['description']
            })
        self._city_cache[city] = forecast
        return forecast

class CityInfo:
    """The city weather"""

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherMap()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

def _main():
    weather_forecast = OpenWeatherMap()
    for i in range(5):
        city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
        city_info.weather_forecast()
    #pprint.pprint(weather_forecast)

if __name__ == "__main__":
    _main()