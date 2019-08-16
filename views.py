from flask import Flask, request, render_template
from modifyuserinput import *
from api import *
from constant import *

app = Flask(__name__)
app.debug = True


class Control:

    def __init__(self, form):
        self.object_wiki = ApiWiki()
        self.object_gmap = ApiGoogleMap()
        self.list_dialog = []
        self.user_interaction = ModifyUserInput()
        self.coordinates = None
        self.user_question = form
        self.loop = True

    def control_if_empty(self, raw_user_input):
        if raw_user_input == "":  # if input is empty
            self.user_interaction.response_from_papybot = GRANDPY_BOT_QUESTION_EMPTY
            self.list_dialog.extend([raw_user_input, self.user_interaction.response_from_papybot])
            self.loop = False
        else:
            self.user_interaction.modification_process(raw_user_input)

    def control_if_google_found_place(self):
        if self.object_gmap.googlemap_json['status'] == 'ZERO_RESULTS' or self.object_gmap.googlemap_json == {}:      # if googlemap not found
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question["question"], self.user_interaction.response_from_papybot])
            self.loop = False

    def control_if_wiki_found_result(self):
        try:  # if something wrong with mediawiki
            self.object_wiki.wiki_procedure_get_pageid(self.user_interaction.input_to_search)
            self.object_wiki.wiki_procedure_get_description(self.object_wiki.page_id)
        except KeyError:
            self.user_interaction.response_from_papybot = GRANDPY_BOT_DONT_UNDERSTAND
            self.list_dialog.extend([self.user_question["question"], self.user_interaction.response_from_papybot])
            self.loop = False

    def last_step(self):
        self.user_interaction.get_random_response_from_papybot()
        self.list_dialog.extend(
            [self.user_question["question"], self.user_interaction.response_from_papybot + self.object_wiki.description])
        return render_template('dialog.html', dialog_to_show=self.list_dialog, gmap_key=self.object_gmap.googlemap_key,
                               latitude=self.coordinates[0], longitude=self.coordinates[1])


@app.route('/home/', methods=['GET'])
def home_get():
    return render_template('home.html')


@app.route('/home/', methods=['POST'])
def home_post():

    object_control = Control(request.form)
    user_question = request.form
    raw_user_input = user_question["question"]

    if object_control.loop is True:
        object_control.control_if_empty(raw_user_input)
        if object_control.loop is True:
            object_control.coordinates = object_control.object_gmap.gmap_comm(object_control.user_interaction.input_to_search)
            object_control.control_if_google_found_place()
            if object_control.loop is True:
                object_control.control_if_wiki_found_result()
                result = object_control.last_step()
                return result
    return render_template('dialog.html', dialog_to_show=object_control.list_dialog)


if __name__ == "__main__":
    app.run()
