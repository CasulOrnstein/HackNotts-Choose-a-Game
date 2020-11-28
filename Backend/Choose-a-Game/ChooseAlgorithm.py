import random
import itertools
from flask import jsonify

# Input: list of friends { id, name } (including user), each with a list of multiplayer games {id, name} they play
def choose(players):
    # "all" in the context of users selected + the games they play
    allGames = {}
    allPlayers = {}
    allGameIds = set()
    allPlayerIds = []
    for playerId in players:
        for game in playerId.games:
            allGameIds.add(game.id)
            allGames[game.id] = game
        allPlayerIds.append(playerId.id)
        allPlayers[playerId.id] = playerId.name

    scores = chooseHelper(allPlayerIds, allGameIds, [], 0)
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
            gameDict['game'] = allGames[whatPlay.game]
            gameDict['players'] = []
            for playerId in whatPlay.players:
                gameDict['players'].append(allPlayers[playerId])
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
    for game in games:
        playersThatPlayThisGame = [p for p in players if game in p.games]
        playerRange = game.playerRange() ## TODO
        for numPlayers in playerRange:
            for comb in itertools.combinations(playersThatPlayThisGame, numPlayers):
                foundNone = False
                remainingPlayers = [p for p in players if p not in comb]
                remainingGames = [g for g in games if not g == game]
                nextPlayList = playList.copy()
                nextPlayList.append(WhatPlay(game, comb))
                scores += chooseHelper(remainingPlayers, remainingGames, nextPlayList, i + 1)
    if foundNone == True:
        scores.append(PlayScore(playList, (len(players) * 100) - len(games)))
    return scores
