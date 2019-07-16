import os
import random
import requests
from constant import *


class ApiParameters:

    def __init__(self):
        self.r = None
        self.json = None
        self.PARAMETERS = None
        self.lat = None
        self.lon = None
        self.description = None
        self.wikipedia_return = None
        self.googlemap_return = None
        self.googlemap_key = os.environ.get("gmap_key")  # Enter your own variable's name environnement
        # instead of ("gmap_key")
        self.response = None
        self.responce_dont_understand = grandpy_bot_dont_understand

    def generate_parameters_gmaps(self, latitude, longitude):
        """generate paramaters for googlemaps api"""
        self.PARAMETERS = {"location": (latitude, longitude),
                           "key": self.googlemap_key}

    def generate_parameters_wiki(self, input_user):
        """generate paramaters for wikimedia api"""
        self.PARAMETERS = {"action": "query",
                           "format": "json",
                           "titles": input_user,
                           "prop": "coordinates|description"}

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        self.r = requests.get(url, parameters)
        self.json = self.r.json()
        return self.json

    def wiki_comm(self, input_user):
        """wikipedia return info about user input"""
        self.generate_parameters_wiki(input_user)
        self.wikipedia_return = self.get_info(wiki_url, self.PARAMETERS)
        self.get_info_from_json()

    def gmap_comm(self, latitude, longitude):
        """google maps return a map about user input"""
        self.generate_parameters_gmaps(latitude, longitude)
        self.googlemap_return = self.get_info(maps_url, self.PARAMETERS)
        return self.googlemap_return

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
