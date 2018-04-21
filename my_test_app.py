from flask import Flask
from flask import request

from dark_sky import DarkSkyWeather

app = Flask(__name__)
dark_sky_api_key = '2a4d7d84f67ec474128de81e7ca6f974'

@app.route('/weather/current')
def hello_world():
    DarkSkyWeather.set_api_key(dark_sky_api_key)
    city = request.args.get('city')

    if not city:
        return "Please specify City"

    response = DarkSkyWeather.current(city=city)
    return str(response)
