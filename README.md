# get-coordinates-from-WOEID
Retrieve the latitude and longitude of a location from its WOEID (Where On Earth ID).

# Why ??
Sometimes, some services use WOEID (Where On Earth ID) to handle geographical locations.
This is the case of the twitter API and its processing of location trends
(https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available).

To get the coordinates of a location (latitude and longitude), Yahoo provided an API to retrieve a lot of information about a location, such as geographic coordinates.
Unfortunately, the Twitter API provides a link to this API, which is no longer online and has not been supported by Yahoo for a few years.

So this repository is just here to put another way with Yahoo services to get geographic coordinates from a WOEID.
For this, we can use the Yahoo weather service available at this uri: https://www.yahoo.com/news/_tdnews/api/resource/WeatherService;woeids=[2477058].

# A little script

## Install

```bash
$ python3 -m venv venv
$ pip install -r requirements.txt
$ source venv/bin/activate
```

## Example

```bash
(venv) $  python3 get_coordinates_from_WOEID.py 2477058
{"woeid": 2477058, "latitude": 41.823318, "longitude": -71.419357}
```
