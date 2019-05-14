from constant import *
from api import ApiCommunication


class ModifyUserInput:
    """ check user input to found data to exploit"""

    def __init__(self):
        self.user_input = None
        self.user_input_split = None
        self.list_input_user_cleaned = None
        self.input_to_search = None

    def split_text(self, user_input):
        """string to list"""
        self.user_input_split = user_input.split()

    def clean_text(self, user_input_split):
        """clean text of stop words"""
        for word in user_input_split:
            if word not in stop_words:
                    self.list_input_user_cleaned.append(word)

    def format_text_to_search(self, list_input_cleaned):
        """format text for wikipedia API"""
        self.input_to_search = "|".join(list_input_cleaned)

    def modification_process(self):
        self.user_input.split_text(self.user_input)
        self.user_input_split.clean_text(self.user_input_split)
        self.list_input_user_cleaned.format_text_to_search(self.list_input_user_cleaned)


class Interaction:
    """action between user and api"""

    def __init__(self):
        self.wikipedia_return = None
        self.googlemap_return = None
        self.communication = ApiCommunication()
        self.googlemap_key = None

    def wiki_comm(self, input_user):
        """wikipedia return info about user input"""
        PARAMETERS = self.communication.generate_parameters_wiki(input_user)
        self.wikipedia_return = self.communication.get_info(wiki_url, PARAMETERS)
        return self.wikipedia_return

    def gmap_comm(self, latitude, longitude):
        """google maps return a map about user input"""
        PARAMETERS = self.communication.generate_parameters_gmaps(latitude, longitude)
        self.googlemap_return = self.communication.get_map(maps_url, PARAMETERS)
        return self.googlemap_return
