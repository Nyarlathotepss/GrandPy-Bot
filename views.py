from flask import Flask, request, render_template
from modifyuserinput import *
from api import *

app = Flask(__name__)
app.debug = False
object_wiki = ApiWiki()
object_gmap = ApiGoogleMap()
list_dialog = []


@app.route('/home/', methods=['GET'])
def accueil_get():
    return render_template('home.html')


@app.route('/home/', methods=['POST'])
def accueil_post():
    user_interaction = ModifyUserInput()
    user_question = request.form
    user_interaction.user_input = user_question["question"]
    user_interaction.modification_process()
    try:
        object_wiki.wiki_comm(user_interaction.input_to_search)
    except KeyError:
        list_dialog.extend([user_question["question"], object_wiki.response_dont_understand])
        return render_template('dialog.html', dialog_to_show=list_dialog)
    object_wiki.get_response_from_papybot()
    list_dialog.extend([user_question["question"], object_wiki.response + object_wiki.description])
    print(list_dialog)
    return render_template('dialog.html', dialog_to_show=list_dialog, gmap_key=object_gmap.googlemap_key,
                           latitude=object_gmap.lat, longitude=object_gmap.lon)


if __name__ == "__main__":
    app.run()
