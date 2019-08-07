import os, requests, json, wikipedia, constant


class ApiWiki:

    def __init__(self):
        self.page_id = str
        self.description = str

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
        page_id = None
        data = json
        print(data)
        pages = data['query']['search']
        for k, v in enumerate(pages):
            page_id = str(v['pageid'])
        return page_id

    def get_description_from_json(self, json):
        """get the pageid about input_user from .json"""
        data = json
        pages = data['query']['pages']
        print(pages)
        for k, v in pages.items():
            self.description = str(v['description'])

    def wiki_procedure_get_pageid(self, input_user):
        parameters = self.generate_parameters_wiki_1turn(input_user)
        wiki_json = self.get_info(constant.wiki_url, parameters)
        self.page_id = self.get_pageid_from_json(wiki_json)

    def wiki_procedure_get_description(self, page_id):
        parameters = self.generate_parameters_wiki_2turn(page_id)
        wiki_json = self.get_info(constant.wiki_url, parameters)
        self.get_description_from_json(wiki_json)


class ApiGoogleMap:

    def __init__(self):
        self.googlemap_key = os.environ.get("gmap_key")  # Enter your own variable's name environnement
        # instead of ("gmap_key")
        self.googlemap_json = None
        self.url_apigmap_search = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        self.url_apigmap_display_id = "https://maps.googleapis.com/maps/api/place/details/json?"

    def generate_parameters_gmaps_to_search(self, string):
        """generate paramaters for googlemaps api"""
        paramters = {"input": string,
                     "inputtype": "textquery",
                     "key": self.googlemap_key,
                     "fields": "geometry"}
        return paramters

    def get_info(self, url, parameters):
        """get informations from api and return a json"""
        r = requests.get(url, parameters)
        json = r.json()
        return json

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
