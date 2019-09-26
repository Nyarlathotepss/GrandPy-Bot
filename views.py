from flask import Flask, jsonify, render_template, request
from control import Control

app = Flask(__name__)
app.debug = True


@app.route('/home/', methods=['GET'])
def home_get():
    return render_template('home.html')


@app.route('/home/', methods=['POST'])
def home_post():
    object_control = Control()
    object_control.user_question = request.get_json()
    object_control.all_steps()
    if object_control.case == 0:
        return jsonify(dialog_to_show=object_control.list_dialog, gmap_key=object_control.object_gmap.googlemap_key,
                       latitude=object_control.object_gmap.googlemap_coordinates[0],
                       longitude=object_control.object_gmap.googlemap_coordinates[1])
    else:
        return jsonify(dialog_to_show=object_control.list_dialog)


if __name__ == "__main__":
    app.run()
