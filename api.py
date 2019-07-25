import os
import random
import requests
from constant import *


class ApiWiki:

    def __init__(self):
        self.lat = None
        self.lon = None
        self.description = None
        self.wikipedia_return = None
        self.response = None
        self.response_dont_understand = grandpy_bot_dont_understand

    def generate_parameters_wiki(self, input_user):
        """generate paramaters for wikimedia api"""
        PARAMETERS = {"action": "query",
                      "format": "json",
                      "titles": input_user,
                      "prop": "coordinates|description"}
        return PARAMETERS

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        r = requests.get(url, parameters)
        json = r.json()
        return json

    def wiki_comm(self, input_user):
        """wikipedia return info about user input"""
        parameters = self.generate_parameters_wiki(input_user)
        self.wikipedia_return = self.get_info(wiki_url, parameters)
        self.get_info_from_json()

    def get_info_from_json(self):
        """get the localization from .json (wikipedia)"""
        DATA = self.wikipedia_return
        print(DATA)
        PAGES = DATA['query']['pages']
        for k, v in PAGES.items():
            self.lat = str(v['coordinates'][0]['lat'])
            self.lon = str(v['coordinates'][0]['lon'])
            self.description = str(v['description'])

    def get_response_from_papybot(self):
        """Build the grandpy response"""
        self.response = random.choice(grandpy_bot_responses)


class ApiGoogleMap:

    def __init__(self):
        self.googlemap_key = os.environ.get("gmap_key")  # Enter your own variable's name environnement
        # instead of ("gmap_key")
        self.googlemap_return = None
        self.lat = None
        self.lon = None

    def generate_parameters_gmaps(self, latitude, longitude):
        """generate paramaters for googlemaps api"""
        PARAMETERS = {"location": (latitude, longitude),
                      "key": self.googlemap_key}
        return PARAMETERS

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        r = requests.get(url, parameters)
        json = r.json()
        return json

    def gmap_comm(self, latitude, longitude):
        """google maps return a map about user input"""
        parameters = self.generate_parameters_gmaps(latitude, longitude)
        self.googlemap_return = self.get_info(maps_url, parameters)
        return self.googlemap_return
