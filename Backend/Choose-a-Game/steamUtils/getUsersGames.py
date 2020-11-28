import requests

def getUsersGames(apiKey, userId):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apiKey}&steamid={userId}"
    games = []
    try:
        response = requests.get(url).json()
        games = response["response"]["games"]
    except:
        print("Failed to get games")
    
    return [game["appid"] for game in games]