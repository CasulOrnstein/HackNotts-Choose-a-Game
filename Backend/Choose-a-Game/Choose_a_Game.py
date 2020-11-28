import flask
from flask import request, jsonify
import requests
from steam.steamid import SteamID
from steam.webapi import WebAPI
from APIKey import apiKey

from steamUtils.getUsersFriends import getUsersFriends
from steamUtils.getUsersGames import getUsersGames
from steamUtils.getMultiplayerGames import getMultiplayerGames

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# A route to return all of the available entries in our catalog.
@app.route('/api/friends', methods=['GET'])
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
def getGames():
    if 'friends' in request.args:
        friendsStr = request.args['friends']
    else:
        return "Error: No friends provided. Please specify a name."

    # friends = friendsStr.split(',')
    friends = [76561198044229271]
    friends_games = {}
    for friendId in friends:
        games = getUsersGames(apiKey, friendId)
        print(games)
        friends_games[str(friendId)] = getMultiplayerGames(games)

    return jsonify(friends_games)

app.run()