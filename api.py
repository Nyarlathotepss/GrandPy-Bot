import os, requests, constant


class ApiWiki:
    """class for communication with wikimedia api"""
    def __init__(self):
        self.page_id = str()
        self.description = str()
        self.json_page_id = None
        self.json_description = None

    def generate_parameters_wiki_1turn(self, input_user):
        """generate paramaters for wikimedia api to get page id with name place"""
        parameters = {"action": "query",
                      "format": "json",
                      "list": "search",
                      "srsearch": input_user,
                      "srlimit": "1"}

        return parameters

    def generate_parameters_wiki_2turn(self, page_id):
        """generate paramaters for wikimedia api to get description with page id"""
        parameters = {"action": "query",
                      "format": "json",
                      "prop": "description|coordinates",
                      "pageids": page_id}

        return parameters

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        r = requests.get(url, parameters)
        json = r.json()
        return json

    def get_pageid_from_json(self, json):
        """get the pageid about input_user from .json"""
        data = json
        print(data)
        pages = data['query']['search']
        for k, v in enumerate(pages):
            self.page_id = str(v['pageid'])

    def get_description_from_json(self, json):
        """get the pageid about input_user from .json"""
        data = json
        print(data)
        pages = data['query']['pages']
        for k, v in pages.items():
            self.description = str(v['description'])

    def wiki_procedure_request_get_pageid(self, input_user):
        parameters = self.generate_parameters_wiki_1turn(input_user)
        self.json_page_id = self.get_info(constant.WIKI_URL, parameters)

    def wiki_procedure_requests_get_description(self, page_id):
        parameters = self.generate_parameters_wiki_2turn(page_id)
        self.json_description = self.get_info(constant.WIKI_URL, parameters)


class ApiGoogleMap:
    """class for communication with google map api"""
    def __init__(self):
        self.googlemap_key = os.environ.get("gmap_key")  # Enter your own variable's name environnement
        # instead of ("gmap_key")
        self.googlemap_json = None
        self.url_apigmap_search = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    def generate_parameters_gmaps_to_search(self, string):
        """generate paramaters for googlemaps api"""
        parameters = {"input": string,
                      "inputtype": "textquery",
                      "key": self.googlemap_key,
                      "fields": "geometry"}
        return parameters

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        r = requests.get(url, parameters)
        return r.json()

    def gmap_comm(self, string):
        """google maps return a map about user input"""
        parameters = self.generate_parameters_gmaps_to_search(string)
        self.googlemap_json = self.get_info(self.url_apigmap_search, parameters)
        coordinates = self.get_coordinates_from_json(self.googlemap_json)
        return coordinates

    def get_coordinates_from_json(self, json):
        """get the localization from .json (wikipedia)"""
        data = json
        lat, lon = str, str
        pages = data['candidates']
        for k, v in enumerate(pages):
            lat = str(v['geometry']['location']["lat"])
            lon = str(v['geometry']['location']['lng'])
        return lat, lon
