import requests
import json
from io import BytesIO
from PIL import Image

def get_data():
#Get latitude and longitude of nearest city from Air Visual
    url = "http://api.airvisual.com/v2/nearest_city?key=1626af95-b1e5-41e9-9e18-8991b754eb87"
    response = requests.request('GET', url)
    raw_data = json.loads(response.text)
    measurements = []
    #print(raw_data)
    lon = raw_data["data"]["location"]["coordinates"][0]
    lat = raw_data["data"]["location"]["coordinates"][1]
    print("Latitude is ", lat, "Longitude is ", lon)
    # Get weather from OpenWeather using latitude and longitude from Air Visua;
    exclude = "current,minutely,daily"
    api_key = "a68a0ee8420eb5ffcb2a5ce643107da7"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}".format(lat,lon,exclude, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
   # print(data)
    return data
   
