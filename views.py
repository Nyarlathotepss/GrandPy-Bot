from flask import Flask, request, render_template
from modifyuserinput import *
from api import *
from constant import *

app = Flask(__name__)
app.debug = True
object_wiki = ApiWiki()
object_gmap = ApiGoogleMap()
list_dialog = []


@app.route('/home/', methods=['GET'])
def home_get():
    return render_template('home.html')


@app.route('/home/', methods=['POST'])
def home_post():

    user_interaction = ModifyUserInput()
    user_question = request.form
    raw_user_input = user_question["question"]
    if raw_user_input == "":                                        # if input is empty
        user_interaction.response_from_papybot = grandpy_bot_question_empty
        list_dialog.extend([raw_user_input, user_interaction.response_from_papybot])
        return render_template('dialog.html', dialog_to_show=list_dialog)

    user_interaction.modification_process(raw_user_input)
    coordinates = object_gmap.gmap_comm(user_interaction.input_to_search)

    if object_gmap.googlemap_json['status'] == 'ZERO_RESULTS':      # if googlemap not found
        user_interaction.response_from_papybot = grandpy_bot_dont_understand
        list_dialog.extend([user_question["question"], user_interaction.response_from_papybot])
        return render_template('dialog.html', dialog_to_show=list_dialog)

    try:                                                            # if something wrong with mediawiki
        object_wiki.wiki_procedure_get_pageid(user_interaction.input_to_search)
        object_wiki.wiki_procedure_get_description(object_wiki.page_id)
    except KeyError:
        user_interaction.response_from_papybot = grandpy_bot_dont_understand
        list_dialog.extend([user_question["question"], user_interaction.response_from_papybot])
        return render_template('dialog.html', dialog_to_show=list_dialog)

    user_interaction.get_random_response_from_papybot()
    list_dialog.extend([user_question["question"], user_interaction.response_from_papybot + object_wiki.description])
    return render_template('dialog.html', dialog_to_show=list_dialog, gmap_key=object_gmap.googlemap_key,
                           latitude=coordinates[0], longitude=coordinates[1])


if __name__ == "__main__":
    app.run()
