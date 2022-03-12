import requests
import json
from io import BytesIO
from PIL import Image

def get_data():
#Get latitude and longitude of nearest city from Air Visual
    url = "http://api.airvisual.com/v2/nearest_city?key=your_AirVisula_API_key"
    response = requests.request('GET', url)
    raw_data = json.loads(response.text)
    measurements = []
    #print(raw_data)
    lon = raw_data["data"]["location"]["coordinates"][0]
    lat = raw_data["data"]["location"]["coordinates"][1]
    print("Latitude is ", lat, "Longitude is ", lon)
    # Get weather from OpenWeather using latitude and longitude from Air Visua;
    exclude = "current,minutely,daily"
    api_key = "Your Openweather API key"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}".format(lat,lon,exclude, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
   # print(data)
    return data
   
