import flask
from flask import request, jsonify
import requests
from steam.steamid import SteamID
from steam.webapi import WebAPI

app = flask.Flask(__name__)
app.config["DEBUG"] = True
theapi = "96E0B2A6BBCF8793BDC4619BABEB6C59"
api = WebAPI(key=theapi)

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

    steamId = SteamID.from_url('https://steamcommunity.com/id/' + name)

    api.ISteamWebAPIUtil.GetServerInfo()
    res = api.call('ISteamWebAPIUtil.GetServerInfo')

    theurl = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + theapi + '&steamid=' + str(steamId) + '&relationship=friend'

    friendlist = requests.get(theurl).json()['friendslist']['friends']

    steamidlist = []
    # For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
    for i in range(len(friendlist)):
        steamidlist.append(friendlist[i]['steamid'])

    # Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
    joinedsids = ','.join(steamidlist)

    ## Function I wrote to print out friend data in json format.
    #+ call the function printFriendInfo() by passing a comma-separated
    #+ list of SteamID64 IDs, e.g. (the following IDs are fake):
    #+      printFriendInfo(09812409,234890234,0982130)
    def getFriendInfo(ids):
        userurl = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + theapi + '&steamids=' + ids
        userget = requests.get(userurl).json()['response']
        return userget
        #for i in range(len(userget['players'])):
        #    print(userget['players'][i])

    # This function gets 
    def printOnlineFriends(ids):
        userurl = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + theapi + '&steamids=' + ids
        userget = requests.get(userurl).json()['response']

        onlineDict = {}
        global maxnamelen
        maxnamelen = 0
        for i in range(len(userget['players'])):
            tonli = userget['players'][i]['personastate']
            if tonli == 1:
                #They're online. Are they playing a game? Does the 'gameextrainfo' key exist?
                if 'gameextrainfo' in userget['players'][i]:
                    sname = userget['players'][i]['personaname']
                    sgame = userget['players'][i]['gameextrainfo']
                    onlineDict.update( {sname : sgame} )
                    if len(sname) > maxnamelen:
                        maxnamelen = int(len(sname))
                # onlineArray.append(userget['players'][i]['personaname'])
            else:
                # not online and not playing a game. continue to the next friend
                continue
    
        sortDict = sorted(onlineDict.items(), key=lambda z: z[1])
        for i in sorted (onlineDict.keys()):
        # for i in sorted (sortDict):
            tspaces = ""
            lennamediff = (maxnamelen - len(i)) + 2
            for x in range(lennamediff):
                tspaces += ' '
            print(i + tspaces, "[" + onlineDict[i] + "]")
            # END printOnlineFriends

    return getFriendInfo(joinedsids)

app.run()