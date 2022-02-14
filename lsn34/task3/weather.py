import requests
import argparse
from datetime import datetime


argparser = argparse.ArgumentParser(description="Weather app")
argparser.add_argument("-c", "--city", help="City name", required=True)
args = vars(argparser.parse_args())

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

params = {
    "q": {f"{args['city']}"},
    "appid": "2e53fa1f2d3e9191ec730cd0e44fd06b",
    "units": "metric",
}

response = requests.get(BASE_URL, params=params).json()


def show_result(data):
    print(
        f"""
    City: {data['name']}
    Temperature: {data['main']['temp']} °C
    Weather: {data['weather'][0]['description']} 
    Sunset: {datetime.utcfromtimestamp(int(data['sys']['sunset'])).strftime(
                "%Y-%m-%d %H:%M:%S"
            )} UTC
    """
    )


show_result(response)
