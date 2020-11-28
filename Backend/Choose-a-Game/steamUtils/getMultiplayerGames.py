import json
import requests

def getAppInfo(appId):
    url = f"https://store.steampowered.com/api/appdetails?appids={appId}"
    try:
        response = requests.get(url).json()
        return response[str(appId)]["data"]
    except:
        print("Failed to get categories")
        return {}


def getMultiplayerGames(appCacheOriginal, appList):
    appCache = appCacheOriginal.copy()
    cacheModified = False
    gamesList = []
    for appId in appList:
        if str(appId) in appCache:
            if appCache[str(appId)]["isMultiplayer"]:
                gamesList.append(appCache[str(appId)])
        else:
            appData = getAppInfo(appId)
            is_multiplayer = isTaggedMultiplayer(appData)
            gameInfo = { "isMultiplayer": is_multiplayer }
            if is_multiplayer:
                gameInfo = getGameInfo(appData)
                gameInfo["isMultiplayer"] = True
                gamesList.append(gameInfo)

            appCache[str(appId)] = gameInfo
            cacheModified = True
    
    if cacheModified:
        # Overwrite cache
        print("Overwriting Cache")
        with open('app_cache.json', 'w') as outfile:
            json.dump(appCache, outfile)
    return gamesList

default_gameInfo = {
    "Online": "4",
    "Couch": "4",
    "Combo": "4"
}

def getMaxPlayers(appId):
    with open('max_players_lookup.json') as json_file:
        max_players_lookup = json.load(json_file)
        return max_players_lookup.get(str(appId), default_gameInfo)

multiplayer_categories = [
    "Multi-player",
    "Cross-Platform Multiplayer",
    "Co-op",
    "Online Co-op",
    "PvP",
    "Online PvP",
    "LAN PvP",
    "Shared/Split Screen PvP",
    "LAN Co-op",
    "Shared/Split Screen Co-op",
    "Shared/Split Screen",
    "Cross-Platform Multiplayer"
]

def isTaggedMultiplayer(appData):
    try:
        categories_withids = appData["categories"]
        categories = [i["description"] for i in categories_withids]
        is_multiplayer = any(cat in multiplayer_categories for cat in categories)
        return is_multiplayer
    except:
        print("Failed to get categories")
        return False

def getGameInfo(appData):
    if "steam_appid" not in appData:
        print("Failed to extract id")
        return {}
    
    appId = appData["steam_appid"]
    maxPlayers = getMaxPlayers(appId)
    output = { 
        "appId": appId,
        "url": f"https://store.steampowered.com/app/{appId}/",
        "maxCouchPlayers": maxPlayers["Couch"],
        "maxOnlinePlayers": maxPlayers["Online"],
        "maxComboPlayers": maxPlayers["Combo"]
    }

    try:
        # Update output 
        output["headerImage"] = appData["header_image"] 
        output["name"] = appData["name"]
    except:
        print("Failed to lookup game on steam")
        return {}
    
    return output