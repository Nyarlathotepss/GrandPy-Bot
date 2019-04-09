from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.debug = True


@app.route('/accueil/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'GET':
        return render_template('accueil.html')

    else:
        return request.form["adress"]


if __name__ == "__main__":
    app.run()
