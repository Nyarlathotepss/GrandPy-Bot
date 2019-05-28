from flask import Flask, request, render_template, url_for
from main import ModifyUserInput
from api import ApiParameters
import os

app = Flask(__name__)
app.debug = True
Api_Obj = ApiParameters()
list_dialog = []
gmap_key = os.environ.get("gmap_key")  # Enter your own variable's name environement


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        return render_template('accueil.html')

    else:
        list_number_loop = 0
        user_interaction = ModifyUserInput()
        user_question = request.form
        user_interaction.user_input = user_question["question"]
        user_interaction.modification_process()
        Api_Obj.wiki_comm(user_interaction.input_to_search)
        Api_Obj.get_response_from_papybot()
        list_dialog.extend([user_question["question"], Api_Obj.response + Api_Obj.description])
        print(list_dialog)
        return render_template('dialog.html', dialog_to_show=list_dialog, gmap_key=Api_Obj.googlemap_key,
                               latitude=Api_Obj.lat, longitude=Api_Obj.lon)


if __name__ == "__main__":
    app.run()
