import requests


class GoogleMapsApi:

    def __init__(self):
        self.request = None
        self.PARAMETERS = {}


class WikipediaApi:

    def __init__(self):
        self.r = requests.session()
        self.WIKI_PARAMETERS = {"action": "query",
                                "format": "json"}

    def get_info(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r.json()
