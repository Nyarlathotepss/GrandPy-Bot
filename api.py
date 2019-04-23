import requests


class ApiCommunication:

    def __init__(self):
        self.r = None
        self.PARAMETERS = {}
        self.lat = None
        self.lon = None

    def generate_parameters_gmaps(self, latitude, longitude):
        self.PARAMETERS = {"location": (latitude, longitude),
                           "key": "maclef"}

    def generate_parameters_wiki(self, input_user):
        self.PARAMETERS = {"action": "query",
                           "format": "json",
                           "titles": input_user,
                           "prop": "coordinates"}

    def get_map(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r

    def get_info(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r.json()
