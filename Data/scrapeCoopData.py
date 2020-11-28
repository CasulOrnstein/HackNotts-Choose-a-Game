import requests
import json
from bs4 import BeautifulSoup

all_games = []

for page in range(1,84):
    URL = f'https://www.co-optimus.com/ajax/ajax_games.php?game-title-filter=&system=4&countDirection=&playerCount=&page={page}&sort=&sortDirection='
    data = requests.get(URL)
    soup = BeautifulSoup(data.content, 'html.parser')
    rows = soup.find_all('tr')

    for row in rows:
        results = {}

        # Find the games name
        cells = row.find_all('td')
        if cells:
            if cells[0]:
                strong = cells[0].find('strong')
                results["Title"] = strong.text
            
            # Find Online number
            if cells[1]:
                results["Online"] = cells[1].text

            # Find Couch number
            if cells[2]:
                results["Couch"] = cells[2].text
            
            # Find Combo number
            if cells[3]:
                results["Combo"] = cells[3].text

            all_games.append(results)

print(len(all_games))
with open('all_games.json', 'w') as outfile:
    json.dump(all_games, outfile)