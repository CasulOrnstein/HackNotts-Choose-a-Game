import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/games', methods=['GET'])
def api_name():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name provided. Please specify a name."

    return name;

    #return jsonify(books)

app.run()