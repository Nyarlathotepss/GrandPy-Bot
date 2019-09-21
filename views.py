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
    object_control.first_step()
    object_control.second_step()
    object_control.third_step()
    object_control.last_step()

    if object_control.loop is True:
        return jsonify(dialog_to_show=object_control.list_dialog, gmap_key=object_control.object_gmap.googlemap_key,
                       latitude=object_control.coordinates[0], longitude=object_control.coordinates[1])
    else:
        return jsonify(dialog_to_show=object_control.list_dialog)


if __name__ == "__main__":
    app.run()
