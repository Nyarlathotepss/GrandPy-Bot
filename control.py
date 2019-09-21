from modifyuserinput import *
from api import *
from constant import *


class Control:
    """Several tests to control if user's question or json from api are correct """
    def __init__(self):
        self.object_wiki = ApiWiki()
        self.object_gmap = ApiGoogleMap()
        self.list_dialog = []
        self.user_interaction = ModifyUserInput()
        self.coordinates = None
        self.user_question = None
        self.loop = True

    def control_if_empty(self):
        """check if user's question are empty"""
        if self.user_question == "":  # if input is empty
            self.user_interaction.response_from_papybot = GRANDPY_BOT_QUESTION_EMPTY
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False
        else:
            self.user_interaction.modification_process(self.user_question)

    def control_if_google_found_place(self):
        """check if google map api found a place"""
        if self.object_gmap.googlemap_json == {} or self.object_gmap.googlemap_json['status'] == 'ZERO_RESULTS':
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False

    def control_if_wiki_found_page_id(self):
        """check if wikimedia found a pageid about place"""
        try:  # if something wrong with mediawiki
            self.object_wiki.get_pageid_from_json(self.object_wiki.json_page_id)
        except KeyError:
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False

    def control_if_wiki_found_description(self):
        """check if wikimedia found a description about place"""
        try:  # if something wrong with mediawiki
            self.object_wiki.get_description_from_json(self.object_wiki.json_description)
        except KeyError:
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False

    def first_step(self):
        self.control_if_empty()
        if self.loop is True:
            self.coordinates = self.object_gmap.gmap_comm(self.user_interaction.input_to_search)
            self.control_if_google_found_place()

    def second_step(self):
        if self.loop is True:
            self.object_wiki.wiki_procedure_request_get_pageid(self.user_interaction.input_to_search)
            self.control_if_wiki_found_page_id()

    def third_step(self):
        if self.loop is True:
            self.object_wiki.wiki_procedure_requests_get_description(self.object_wiki.page_id)
            self.control_if_wiki_found_description()

    def last_step(self):
        """if all previously steps are OK >>> do last step to display the result """
        if self.loop is True:
            self.user_interaction.get_random_response_from_papybot()
            self.list_dialog.extend(
                [self.user_question, self.user_interaction.response_from_papybot + self.object_wiki.description])