import requests
import json
import pprint


# testing

def getLeaderboard(region):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)
    if status == 400:
        print("Request Error (missing query).")
    elif status == 403:
        print("Forbidden to connect to Riot API (mainly maintenance and side patches).")
    elif status == 404:
        print("The requested entity was not found.")
    elif status == 408:
        print("Timeout while fetching data.")
    elif status == 429:
        print("Rate limit reached")
    elif status == 503:
        print("Riot API seems to be down, API unable to connect.")
    else:
        print("API fully operational.")



    getLeaderboard = {
        0: {
            "Name": ["test"],
            "Tag": ["123"],
            "Wins": ["---"]
        }
    }

    for i in range(1, 1001):
        getLeaderboard[i] = {
            "Name": [raw[(i - 1)]['gameName']],
            "Tag": [raw[(i - 1)]['tagLine']],
            "Wins": [raw[(i - 1)]['numberOfWins']]
        }
    return getLeaderboard

ans = getLeaderboard("eu")
pp = pprint.PrettyPrinter(sort_dicts=False)
pp.pprint(ans)
