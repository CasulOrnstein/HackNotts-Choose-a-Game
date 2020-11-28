from APIKey import apiKey
import requests
from steam.steamid import SteamID
from steam.webapi import WebAPI
from flask import request, jsonify

def getUsersNames(userIds):
    idsStr = ','.join(userIds)
    getUrl = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apiKey}&steamids={idsStr}'
    playerlist = requests.get(getUrl).json()['response']['players']
    nameDict = {}
    for p in playerlist:
        nameDict[p['steamid']] = p['personaname']

    return nameDict