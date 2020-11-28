import requests
import cloudscraper
import json
from bs4 import BeautifulSoup

final_results = []
index = 1147

with open('all_games.json') as json_file:
    data = json.load(json_file)
    print("LOADED DATA")
    for game in data[640:1146]:
        steamId = None
        game_name = game["Title"]
        URL = f'https://steamspy.com/search.php?s={game_name.replace(" ", "+")}'
        data = requests.get(URL)
        soup = BeautifulSoup(data.content, 'html.parser')
        results = soup.find(class_='col-md-4 col-lg-4 col-sm-4 col-xs-12 col-sm-height m-l-15')
        if results:
            link = results.find('a', href=True)
            if link:
                steamId = link['href'].split('/')[-1]
        
        game_copy = game.copy()
        if steamId:
            game_copy["SteamId"] = steamId
        print(game_copy)
        print(f"Game {index} of 206X")
        final_results.append(game_copy)
        index = index + 1

with open('all_games_with_ids.json', 'w') as outfile:
    json.dump(final_results, outfile)