from flask import Flask
from flask import request

from dark_sky import DarkSkyWeather
from forecast import Forecast

app = Flask(__name__)
dark_sky_api_key = '2a4d7d84f67ec474128de81e7ca6f974'
DarkSkyWeather.set_api_key(dark_sky_api_key)


@app.route('/weather/currently')
def get_currently_forecast():
    city = request.args.get('city')

    response = DarkSkyWeather.currently(city=city)
    forecast_data = Forecast(timestamp=response["currently"]["time"],
                            temperature=response["currently"]["temperature"])
    return str(forecast_data)


@app.route('/weather/daily')
def get_daily_forecast():
    city = request.args.get('city')

    response = DarkSkyWeather.daily(city=city)
    # response processing
    return str(response)


@app.route('/weather/hourly')
def get_hourly_forecast():
    city = request.args.get('city')

    response = DarkSkyWeather.hourly(city=city)
    # response processing
    return str(response)


@app.route('/weather')
def get_forecast():
    city = request.args.get('city')

    response = DarkSkyWeather.all(city=city)
    # response processing
    return str(response)
