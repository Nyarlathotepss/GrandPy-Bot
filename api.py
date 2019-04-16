import requests


class ApiCommunication:

    def __init__(self):
        self.r = requests.session()
        self.PARAMETERS = {}

    def generate_parameters_gmaps(self, input_user):
        self.PARAMETERS = {"query": input_user,
                           "key": "AIzaSyAdO62_IhTqYg8IROK76ACbzm-xnbhyC2g"}

    def generate_parameters_wiki(self, input_user):
        self.PARAMETERS = {"action": "query",
                           "format": "json",
                           "text": input_user}

    def get_map(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r

    def get_info(self, url, parameters):
        self.r = self.r.get(url, parameters)
        return self.r.json()
