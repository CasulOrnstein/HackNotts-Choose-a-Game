import json

results = {}

with open('all_games_with_ids.json') as json_file:
    data = json.load(json_file)
    for game in data:
        if game.get("SteamId", None) is not None:
            if game["SteamId"] not in results:
                results[game["SteamId"]] = {
                    "Title": game["Title"],
                    "Online": game["Online"],
                    "Couch": game["Couch"],
                    "Combo": game["Combo"]
                }

with open('max_players_lookup.json', 'w') as outfile:
    json.dump(results, outfile)