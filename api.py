import requests


class GoogleMapsApi:

    def __init__(self):
        self.request = None


class WikipediaApi:

    def __init__(self):
        self.r = requests.session()

    def get_info(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r.jason()
