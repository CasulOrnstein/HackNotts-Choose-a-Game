import flask
from flask import request, jsonify
import requests
from steam.steamid import SteamID
from steam.webapi import WebAPI
import APIKey

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = WebAPI(key=APIKey.theapi)

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

    if 'includeoffline' in request.args:
        includeOffline = int(request.args['includeoffline']) != 0
    else:
        includeOffline = False

    steamId = SteamID.from_url('https://steamcommunity.com/id/' + name)

    api.ISteamWebAPIUtil.GetServerInfo()
    res = api.call('ISteamWebAPIUtil.GetServerInfo')

    theurl = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + APIKey.theapi + '&steamid=' + str(steamId) + '&relationship=friend'

    friendlist = requests.get(theurl).json()['friendslist']['friends']

    steamidlist = []
    # For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
    for i in range(len(friendlist)):
        steamidlist.append(friendlist[i]['steamid'])

    # Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
    joinedsids = ','.join(steamidlist)

    userurl = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + APIKey.theapi + '&steamids=' + joinedsids
    userget = requests.get(userurl).json()['response']

    friendsRet = []
    for i in range(len(userget['players'])):
        online = userget['players'][i]['personastate']
        if (online == 1 or includeOffline):
            friend = {}
            friend["personaname"] = userget['players'][i]['personaname']
            friend["steamid"] = userget['players'][i]['steamid']
            friend["avatarmedium"] = userget['players'][i]['avatarmedium']
            friendsRet.append(friend)
        else:
            # not online and not playing a game. continue to the next friend
            continue

    return jsonify(friendsRet)

app.run()