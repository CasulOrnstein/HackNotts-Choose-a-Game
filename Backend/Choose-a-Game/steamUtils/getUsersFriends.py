import requests
from steam.steamid import SteamID
from steam.webapi import WebAPI
from flask import request, jsonify

def getUsersFriends(apiKey, userId, includeOffline = False):
    steamId = SteamID.from_url(f'https://steamcommunity.com/id/{userId}')

    getFriendsUrl = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={apiKey}&steamid={steamId}&relationship=friend'
    friendlist = requests.get(getFriendsUrl).json()['friendslist']['friends']

    steamidlist = []
    # For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
    for i in range(len(friendlist)):
        steamidlist.append(friendlist[i]['steamid'])

    # Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
    joinedsids = ','.join(steamidlist)

    userurl = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apiKey}&steamids={joinedsids}'
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

    dictOut = {}
    dictOut['friends'] = friendsRet
    dictOut['thisuserid'] = steamId
    return dictOut