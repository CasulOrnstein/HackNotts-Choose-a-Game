import random
import itertools
from flask import jsonify

# Input: list of friends { id, name, games } (including user), each with a list of games {id, name, maxCount} they play
def choose(players):
    # "all" in the context of users selected + the games they play
    allGames = {}
    allPlayers = {}
    for player in players:
        gameIds = []
        for game in player['games']:
            allGames[game['appId']] = game
            gameIds.append(game['appId'])
        allPlayers[player['id']] = {'name' : player['name'], 'gameIds' : gameIds }

    scores = chooseHelper(allPlayers, allGames, [], 0)
    random.shuffle(scores)
    scores.sort(key=lambda x:x.score, reverse = False)

    if len(scores) == 0 or len(scores[0].playList) == 0:
        return "Not enough users"

    topXGames = []
    i = 1
    outStr = ""
    minScore = scores[0].score
    scoreCutOff = 50 # don't include games which have fewer people
    gamesPrinted = []
    for score in scores:
        gameAlreadyPrinted = False
        for whatPlay in score.playList:
            if whatPlay.game in gamesPrinted:
                gameAlreadyPrinted = True
                break
        if gameAlreadyPrinted:
            continue

        gamesList = []
        for whatPlay in score.playList:
            gameDict = {}
            gameDict['gamename'] = whatPlay.game['name']
            gameDict['playerNames'] = []
            for player in whatPlay.players:
                gameDict['playerNames'].append(player['name'])
            gamesList.append(gameDict)
            gamesPrinted.append(whatPlay.game)

        topXGames.append(gamesList)
        i += 1
        if (score.score > minScore + scoreCutOff):
            break
        if (i > 6):
            break
    return jsonify(topXGames)

class PlayScore:
    def __init__(self, playList, score):
        self.playList = playList
        self.score = score

class WhatPlay:
    def __init__(self, game, players):
        self.game = game
        self.players = players

def chooseHelper(players, games, playList, i):
    scores = [] 
    foundNone = True
    for gameid, game in games.items():
        playersThatPlayThisGame = [pid for pid, player in players.items() if game['appId'] in player['gameIds']]
        playerRange = range(2, int(game['maxOnlinePlayers']) + 1)
        for numPlayers in playerRange:
            for comb in itertools.combinations(playersThatPlayThisGame, numPlayers):
                foundNone = False
                remainingPlayers = players.copy()
                for pid in comb:
                    del remainingPlayers[pid]
                remainingGames = games.copy()
                del remainingGames[gameid]
                nextPlayList = playList.copy()
                nextPlayList.append(WhatPlay(game, [players[pid] for pid in comb]))
                scores += chooseHelper(remainingPlayers, remainingGames, nextPlayList, i + 1)
    if foundNone == True:
        scores.append(PlayScore(playList, (len(players) * 100) - len(games)))
    return scores
