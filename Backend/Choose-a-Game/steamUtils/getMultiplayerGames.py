import json
import requests

def getMultiplayerGames(appList):
    return [getGameInfo(appId) for appId in appList if isTaggedMultiplayer(appId)]

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

def isTaggedMultiplayer(appId):
    url = f"https://store.steampowered.com/api/appdetails?appids={appId}"
    categories = []
    try:
        response = requests.get(url).json()
        categories_withids = response[str(appId)]["data"]["categories"]
        categories = [i["description"] for i in categories_withids]
    except:
        print("Failed to get categories")
    
    return any(cat in multiplayer_categories for cat in categories)

def getGameInfo(appId):
    maxPlayers = getMaxPlayers(appId)
    output = { 
        "appId": appId,
        "url": f"https://store.steampowered.com/app/{appId}/",
        "maxCouchPlayers": maxPlayers["Couch"],
        "maxOnlinePlayers": maxPlayers["Online"],
        "maxComboPlayers": maxPlayers["Combo"]
    }

    url = f"https://store.steampowered.com/api/appdetails?appids={appId}"
    try:
        response = requests.get(url).json()
        gameData = response[str(appId)]["data"]

        # Update output 
        output["headerImage"] = gameData["header_image"] 
        output["name"] = gameData["name"]
    except:
        print("Failed to lookup game on steam")
    
    return output