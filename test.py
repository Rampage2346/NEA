import requests
import json
import pprint


def getLeaderboard(region):
    global leaderboard

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    leaderboard = {
        0: {
            "Name": ["test"],
            "Tag": ["123"],
            "Wins": ["---"]
            }
    }

    for i in range(1, 1001):

        leaderboard[i] = {
            "Name": [raw[(i-1)]['gameName']],
            "Tag": [raw[(i-1)]['tagLine']],
            "Wins": [raw[(i-1)]['numberOfWins']]
        }


getLeaderboard("eu")

pprint.pprint(leaderboard)
