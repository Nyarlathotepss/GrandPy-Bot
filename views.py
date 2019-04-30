from flask import Flask, request, render_template, url_for
from main import ModifyUserInput

app = Flask(__name__)
app.debug = True
interaction = ModifyUserInput()
la_question = []


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        return render_template('accueil.html')

    else:
        user_question = request.form
        print(user_question)
        la_question.append(user_question["question"])
        return render_template('dialog.html', la_question=la_question)


if __name__ == "__main__":
    app.run()
