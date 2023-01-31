import requests
import json
import pprint


def getAccount(ID, tagline):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    getAccount = {
        'puuid': [raw['data']['puuid']],
        'region': [raw['data']['region']],
        'accountlvl': [raw['data']['account_level']],
        'name': [raw['data']['name']],
        'tag': [raw['data']['tag']],
        'cardS': [raw['data']['card']['small']],
        'cardL': [raw['data']['card']['large']],
        'cardW': [raw['data']['card']['wide']],
        'cardID': [raw['data']['card']['id']],
    }
    return getAccount


ans = getAccount("Rampage", "2346")
pprint.pprint(ans)


def getMMRHistory(region, puuid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr-history/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    getMMRHistory = {
        0: {
            "current_tier": ["---"],
            "imageS": ["---"],
            "imageL": ["---"],
            "tri_up": ["---"],
            "tri_down": ["---"],
            "ranking_in_tier": ["---"],
            "mmr_change": ["---"],
            "elo": ["---"]
        }
    }

    for i in range(1, 6):
        getMMRHistory[i] = {
            "current_tier": [raw['data'][(i - 1)]['currenttierpatched']],
            "imageS": [raw['data'][(i - 1)]['images']['small']],
            "imageL": [raw['data'][(i - 1)]['images']['large']],
            "tri_up": [raw['data'][(i - 1)]['images']['triangle_down']],
            "tri_down": [raw['data'][(i - 1)]['images']['triangle_up']],
            "ranking_in_tier": [raw['data'][(i - 1)]['ranking_in_tier']],
            "mmr_change": [raw['data'][(i - 1)]['mmr_change_to_last_game']],
            "elo": [raw['data'][(i - 1)]['elo']]
        }
    return getMMRHistory


ans2 = getMMRHistory("eu", "59d0eb3c-f800-5840-b043-e0eb26e76ffd")
pprint.pprint(ans2)


def matchID(region, puuid):
    global matchID1, matchID2, matchID3, matchID4, matchID5

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    matchID = {
        0: {
            "matchID": ["---"],
        }
    }

    for i in range(1, 6):
        matchID[i] = {
            "current_tier": [raw['data'][(i - 1)]['metadata']['matchid']],
        }
    return matchID


ans3 = matchID("eu", "59d0eb3c-f800-5840-b043-e0eb26e76ffd")
pprint.pprint(ans3)
