from flask import Flask, request, render_template
from main import ModifyUserInput
from api import ApiParameters

app = Flask(__name__)
app.debug = False
Api_Obj = ApiParameters()
list_dialog = []


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        return render_template('accueil.html')

    else:
        user_interaction = ModifyUserInput()
        user_question = request.form
        user_interaction.user_input = user_question["question"]
        user_interaction.modification_process()
        try:
            Api_Obj.wiki_comm(user_interaction.input_to_search)
        except KeyError:
            list_dialog.extend([user_question["question"], Api_Obj.responce_dont_understand])
            return render_template('dialog.html', dialog_to_show=list_dialog)
        Api_Obj.get_response_from_papybot()
        list_dialog.extend([user_question["question"], Api_Obj.response + Api_Obj.description])
        print(list_dialog)
        return render_template('dialog.html', dialog_to_show=list_dialog, gmap_key=Api_Obj.googlemap_key,
                               latitude=Api_Obj.lat, longitude=Api_Obj.lon)


if __name__ == "__main__":
    app.run()
