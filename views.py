from flask import Flask, request, render_template
from main import ModifyUserInput

app = Flask(__name__)
app.debug = True
interaction = ModifyUserInput()


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        return render_template('accueil.html')

    else:
        interaction.input_user = request.form["user_question"]
        interaction.split_text(interaction.input_user)
        interaction.clean_text(interaction.input_user)


@app.route('/dialog/', methods=['GET', 'POST'])
def dialog():
    if request.method == 'GET':
        return render_template('dialog.html')

    else:
        return render_template('dialog.html')


if __name__ == "__main__":
    app.run()
