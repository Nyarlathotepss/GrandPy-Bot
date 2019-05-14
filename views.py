from flask import Flask, request, render_template, url_for
from main import ModifyUserInput
from api import ApiParameters
import os

app = Flask(__name__)
app.debug = True
user_interaction = ModifyUserInput()
key_gmap = ApiParameters()
la_question = []
gmap_key = os.environ.get("gmap_key")  # Enter your own variable's name environement


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        print(gmap_key)
        return render_template('accueil.html')

    else:
        user_question = request.form
        la_question.append(user_question["question"])
        return render_template('dialog.html', la_question=la_question, gmap_key=key_gmap.googlemap_key)


if __name__ == "__main__":
    app.run()
