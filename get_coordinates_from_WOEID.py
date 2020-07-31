import requests
import json
import sys

def get_coordinates(woeid):
    uri = "https://www.yahoo.com/news/_tdnews/api/resource/WeatherService;woeids=[{}]"
    response = {}
    r = requests.get(uri.format(woeid))
    if r.status_code == 200:
        data = json.loads(r.text)
        location = data['weathers'][0]['location']
        response['woeid'] = location['woeid']
        response['latitude'] = location['latitude']
        response['longitude'] = location['longitude']
    return response

def main():
    coordinates = get_coordinates(sys.argv[1])
    print(json.dumps(coordinates))

if __name__ == "__main__":
    main()
