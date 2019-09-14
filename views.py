from flask import Flask, jsonify, render_template, request
from modifyuserinput import *
from api import *
from constant import *

app = Flask(__name__)
app.debug = True


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

    def last_step(self):
        """if all previously steps are OK >>> do last step to display the result """
        self.user_interaction.get_random_response_from_papybot()
        self.list_dialog.extend(
            [self.user_question, self.user_interaction.response_from_papybot + self.object_wiki.description])


@app.route('/home/', methods=['GET'])
def home_get():
    return render_template('home.html')


@app.route('/home/', methods=['POST'])
def home_post():
    object_control = Control()
    raw_question = request.get_json()
    print(raw_question)
    object_control.user_question = raw_question

    if object_control.loop is True:
        object_control.control_if_empty()
        if object_control.loop is True:
            object_control.coordinates = object_control.object_gmap.gmap_comm(object_control.
                                                                              user_interaction.input_to_search)
            object_control.control_if_google_found_place()
            if object_control.loop is True:
                object_control.object_wiki.wiki_procedure_request_get_pageid(object_control.
                                                                             user_interaction.input_to_search)
                object_control.control_if_wiki_found_page_id()
                if object_control.loop is True:
                    object_control.object_wiki.wiki_procedure_requests_get_description(object_control.object_wiki.page_id)
                    object_control.control_if_wiki_found_description()
                    object_control.last_step()
                    print(object_control.list_dialog, object_control.object_gmap.googlemap_key,
                                   object_control.coordinates[0], object_control.coordinates[1])
                    return jsonify(dialog_to_show=object_control.list_dialog, gmap_key=object_control.object_gmap.googlemap_key,
                                   latitude=object_control.coordinates[0], longitude=object_control.coordinates[1])

    return jsonify(dialog_to_show=object_control.list_dialog)


if __name__ == "__main__":
    app.run()
