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
        self.user_question = None
        self.loop = True
        self.case = int()

    def control_if_empty(self):
        """check if user's question are empty"""
        if self.user_question == "":  # if input is empty
            self.user_interaction.response_from_papybot = GRANDPY_BOT_QUESTION_EMPTY
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False
            self.case = 1
        else:
            self.user_interaction.modification_process(self.user_question)

    def control_if_google_found_place(self):
        """check if google map api found a place"""
        if self.object_gmap.googlemap_json == {} or self.object_gmap.googlemap_json['status'] == 'ZERO_RESULTS':
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False
            self.case = 1

    def control_if_wiki_found_page_id(self):
        """check if wikimedia found a pageid about place"""
        try:  # if something wrong with mediawiki
            self.object_wiki.get_pageid_from_json(self.object_wiki.json_page_id)
        except KeyError:
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False
            self.case = 0

    def control_if_place_is_same_in_both_api(self):
        """control if coordinates in googlemap are same than wikimedia"""
        try:
            self.object_wiki.get_coordinates_from_json(self.object_wiki.json_description)
            compare_result = self.compare_val_coordinates()
            if compare_result is False:
                self.user_interaction.response_from_papybot = GRANDPY_BOT_KNOW_ONLY_PLACE
                self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
                self.loop = False
                self.case = 0
        except KeyError as e:
            print(e)

    def control_if_wiki_found_description(self):
        """check if wikimedia found a description about place"""
        try:  # if something wrong with mediawiki
            self.object_wiki.get_description_from_json(self.object_wiki.json_description)
        except KeyError:
            self.user_interaction.response_from_papybot = GRANDPY_BOT_KNOW_ONLY_PLACE
            self.list_dialog.extend([self.user_question, self.user_interaction.response_from_papybot])
            self.loop = False
            self.case = 0

    def compare_val_coordinates(self, percent=3):
        """compare the two coordinates and give the difference between in percent, if difference is lower than
        parameter percent return True"""
        lat_diff = abs(self.object_gmap.googlemap_coordinates[0] - self.object_wiki.wiki_coordinates[0]) / self.object_gmap.googlemap_coordinates[0] * 100
        lon_diff = abs(self.object_gmap.googlemap_coordinates[1] - self.object_wiki.wiki_coordinates[1]) / self.object_gmap.googlemap_coordinates[1] * 100
        if (lat_diff < percent) and (lon_diff < percent):
            return True
        else:
            return False

    def first_step(self):
        """first step control if user input is empty ot not AND if googlemap search return a result"""
        self.control_if_empty()
        if self.loop is True:
            self.object_gmap.gmap_comm(self.user_interaction.input_to_search)
            self.control_if_google_found_place()

    def second_step(self):
        """second step control if wikimedia have a pageid about input user"""
        if self.loop is True:
            self.object_wiki.wiki_procedure_request_get_pageid(self.user_interaction.input_to_search)
            self.control_if_wiki_found_page_id()

    def third_step(self):
        """third step control if in pageid (second step) found description"""
        if self.loop is True:
            self.object_wiki.wiki_procedure_requests_get_description(self.object_wiki.page_id)
            self.control_if_wiki_found_description()

    def four_step(self):
        """four step check if coordinates in google are same than wikimedia"""
        if self.loop is True:
            self.control_if_place_is_same_in_both_api()

    def last_step(self):
        """if all previously steps are OK >>> do last step to display the result """
        if self.loop is True:
            self.user_interaction.get_random_response_from_papybot()
            self.list_dialog.extend(
                [self.user_question, self.user_interaction.response_from_papybot + self.object_wiki.description])
            self.case = 0

    def all_steps(self):
        self.first_step()
        self.second_step()
        self.third_step()
        self.four_step()
        self.last_step()
