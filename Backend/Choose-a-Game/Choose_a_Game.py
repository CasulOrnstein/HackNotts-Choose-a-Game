import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import requests
import json
from steam.steamid import SteamID
from steam.webapi import WebAPI
from APIKey import apiKey
from ChooseAlgorithm import choose

from steamUtils.getUsersFriends import getUsersFriends
from steamUtils.getUsersGames import getUsersGames
from steamUtils.getMultiplayerGames import getMultiplayerGames
from getUsersNames import getUsersNames

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# A route to return all of the available entries in our catalog.
@app.route('/api/friends', methods=['GET'])
@cross_origin()
def getFriends():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name provided. Please specify a name."

    if 'includeoffline' in request.args:
        includeOffline = int(request.args['includeoffline']) != 0
    else:
        includeOffline = False

    return jsonify(getUsersFriends(apiKey, name, includeOffline))

@app.route('/api/games', methods=['GET'])
@cross_origin()
def getGames():
    friends = []
    if 'friends' in request.args:
        friends = request.args['friends'].split(',')
    else:
        return "Error: No friends provided. Please specify a name."

    friends_games = []
    usernames = getUsersNames(friends)
    with open('app_cache.json') as json_file:
        appCache = json.load(json_file)
        for friendId in friends:
            games = getUsersGames(apiKey, friendId)
            friends_games.append({
                'id' : friendId,
                'name' : usernames[friendId],
                'games' : getMultiplayerGames(appCache, games)
                })

    chosenGames = choose(friends_games)     
    return jsonify(chosenGames)

app.run(debug=True, use_reloader=False)