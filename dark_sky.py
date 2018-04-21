import json
from urllib.parse import urljoin

import requests


class GeoProvider:
    city_coordinates = {
                        "odessa": (46.4736019, 30.603976)
                        }

class DarkSkyWeather:
    api_key = None
    api_url = 'https://api.darksky.net'
    url = None

    @staticmethod
    def set_api_key(key_value):
        if not key_value:
            raise ValueError("Invalid key value")
        DarkSkyWeather.api_key = key_value

    @staticmethod
    def current(city):
        DarkSkyWeather.url = DarkSkyWeather.get_forecast_url(city)

        params = {'exclude': 'daily,minutely,hourly,flags'}
        print(DarkSkyWeather.url)
        response = requests.get(DarkSkyWeather.url, params=params)
        print(response.status_code)

        result = json.loads(response.content.decode('utf-8'))
        print(result)
        return result

    @staticmethod
    def get_forecast_url(city):
        if not DarkSkyWeather.api_key:
            raise ValueError("You should initialise api_key")

        city = city.lower()

        if city not in GeoProvider.city_coordinates:
            raise ValueError("Parameter {} is not a part of a coordinates dictionary.".format(city))

        url_path = 'forecast/{}/{}'.format(DarkSkyWeather.api_key, str(GeoProvider.city_coordinates[city])[1:-1])
        return urljoin(DarkSkyWeather.api_url, url_path)