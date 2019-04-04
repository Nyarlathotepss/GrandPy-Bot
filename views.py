from flask import Flask, request

app = Flask(__name__)
app.debug = True


@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        #affiche la page et le formulaire

    else:
        #traiter les infos
        #afficher le résultat



if __name__ == "__main__":
    app.run()
