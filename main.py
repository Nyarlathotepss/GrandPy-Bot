from constant import *
from api import ApiCommunication


class ModifyUserInput:
    """ check user input to found data to exploit"""

    def __init__(self):
        self.user_input = None
        self.list_user_input = []

    def split_text(self, user_input):
        """string to list"""
        self.user_input = user_input.split()

    def clean_text(self, user_input_split):
        """clean text of stop words"""
        for word in user_input_split:
            if word not in stop_words:
                    self.list_user_input.append(word)


class Interaction:
    """action between user and api"""

    def __init__(self):
        self.wikipedia_return = None
        self.googlemap_return = None
        self.communication = ApiCommunication()

    def wiki_comm(self, input_user):
        """wikipedia return info about user input"""
        PARAMETERS = self.communication.generate_parameters_wiki(input_user)
        self.wikipedia_return =  self.communication.get_info(wiki_url, PARAMETERS)
        return self.wikipedia_return

    def gmap_comm(self, input_user):
        """google maps return a map about user input"""
        PARAMETERS = self.communication.generate_parameters_gmaps(input_user)
        self.googlemap_return = self.communication.get_map(maps_url, PARAMETERS)
        return self.googlemap_return