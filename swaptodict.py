import requests
import json
import pprint


def getAccount(ID, tagline):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
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


# try:
#     ans = getAccount("Rampage", "2346")
#     pp = pprint.PrettyPrinter(sort_dicts=False)
#     pp.pprint(ans)
# except:
#     pass



def matchID(region, puuid):
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
            "matchID": [raw['data'][(i - 1)]['metadata']['matchid']],
        }
    return matchID


# ans3 = matchID("eu", "b2e04f60-68e6-560c-870f-719d47ffaf9d")
# pp = pprint.PrettyPrinter(sort_dicts=False)
# pp.pprint(ans3)


def matchHistory(matchid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    matchHistoryMetadata = {
        1: {
            "map": [raw['data']['metadata']['map']],
            "game_start_patched": [raw['data']['metadata']['game_start_patched']],
            "rounds_played": [raw['data']['metadata']['rounds_played']],
            "mode": [raw['data']['metadata']['mode']],
            "queue": [raw['data']['metadata']['queue']],
            "region": [raw['data']['metadata']['region']],
            "cluster": [raw['data']['metadata']['cluster']]
        }
    }

    matchHistoryPlayerData = {
        0: {
            "puuid": ["---"],
            "name": ["---"],
            "tag": ["---"],
            "team": ["---"],
            "level": ["---"],
            "character": ["---"],
            "current_tier": ["---"],
            "c_casts": ["---"],
            "e_cast": ["---"],
            "q_casts": ["---"],
            "x_casts": ["---"],
            "cardS": ["---"],
            "cardL": ["---"],
            "cardW": ["---"],
            "agent_small": ["---"],
            "agent_bust": ["---"],
            "agent_full": ["---"],
            "agent_kill_feed": ["---"],
            "score": ["---"],
            "kills": ["---"],
            "deaths": ["---"],
            "assists": ["---"],
            "bodyshots": ["---"],
            "headshots": ["---"],
            "legshots": ["---"],
            "damage_made": ["---"],
            "damage_received": ["---"],
            "loadout_avg": ["---"],
            "loadout_overall": ["---"],
            "spent_avg": ["---"],
            "spent_overall": ["---"]
        }
    }

    for i in range(1, 11):
        matchHistoryPlayerData[i] = {
            "puuid": [raw['data']['players']['all_players'][(i - 1)]['puuid']],
            "name": [raw['data']['players']['all_players'][(i - 1)]['name']],
            "tag": [raw['data']['players']['all_players'][(i - 1)]['tag']],
            "team": [raw['data']['players']['all_players'][(i - 1)]['team']],
            "level": [raw['data']['players']['all_players'][(i - 1)]['level']],
            "character": [raw['data']['players']['all_players'][(i - 1)]['character']],
            "current_tier": [raw['data']['players']['all_players'][(i - 1)]['currenttier_patched']],
            "c_casts": [raw['data']['players']['all_players'][(i - 1)]['ability_casts']['c_cast']],
            "e_cast": [raw['data']['players']['all_players'][(i - 1)]['ability_casts']['e_cast']],
            "q_casts": [raw['data']['players']['all_players'][(i - 1)]['ability_casts']['q_cast']],
            "x_casts": [raw['data']['players']['all_players'][(i - 1)]['ability_casts']['x_cast']],
            "cardS": [raw['data']['players']['all_players'][(i - 1)]['assets']['card']['small']],
            "cardL": [raw['data']['players']['all_players'][(i - 1)]['assets']['card']['large']],
            "cardW": [raw['data']['players']['all_players'][(i - 1)]['assets']['card']['wide']],
            "agent_small": [raw['data']['players']['all_players'][(i - 1)]['assets']['agent']['small']],
            "agent_bust": [raw['data']['players']['all_players'][(i - 1)]['assets']['agent']['bust']],
            "agent_full": [raw['data']['players']['all_players'][(i - 1)]['assets']['agent']['full']],
            "agent_kill_feed": [raw['data']['players']['all_players'][(i - 1)]['assets']['agent']['killfeed']],
            "score": [raw['data']['players']['all_players'][(i - 1)]['stats']['score']],
            "kills": [raw['data']['players']['all_players'][(i - 1)]['stats']['kills']],
            "deaths": [raw['data']['players']['all_players'][(i - 1)]['stats']['deaths']],
            "assists": [raw['data']['players']['all_players'][(i - 1)]['stats']['assists']],
            "bodyshots": [raw['data']['players']['all_players'][(i - 1)]['stats']['bodyshots']],
            "headshots": [raw['data']['players']['all_players'][(i - 1)]['stats']['headshots']],
            "legshots": [raw['data']['players']['all_players'][(i - 1)]['stats']['legshots']],
            "damage_made": [raw['data']['players']['all_players'][(i - 1)]['damage_made']],
            "damage_received": [raw['data']['players']['all_players'][(i - 1)]['damage_received']],
            "loadout_avg": [raw['data']['players']['all_players'][(i - 1)]['economy']['loadout_value']['average']],
            "loadout_overall": [raw['data']['players']['all_players'][(i - 1)]['economy']['loadout_value']['overall']],
            "spent_avg": [raw['data']['players']['all_players'][(i - 1)]['economy']['spent']['average']],
            "spent_overall": [raw['data']['players']['all_players'][(i - 1)]['economy']['spent']['overall']]
        }
    return matchHistoryMetadata, matchHistoryPlayerData


# ans4 = matchHistory("6f6d0160-a21f-412d-9f26-b3b17e4ba487")
# pp = pprint.PrettyPrinter(sort_dicts=False)
# pp.pprint(ans4)


def regionVersion(region):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/version/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    regionVersion = {
        1: {
            "status": [raw['status']],
            "version": [raw['data']['version']]
        }
    }
    return regionVersion


# ans5 = regionVersion("eu")
# pp = pprint.PrettyPrinter(sort_dicts=False)
# pp.pprint(ans5)

def getMMRHistory(region, puuid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr-history/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # errorCheck(status)

    getMMRHistoryDict = {
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
        getMMRHistoryDict[i] = {
            "current_tier": [raw['data'][(i - 1)]['currenttierpatched']],
            "imageS": [raw['data'][(i - 1)]['images']['small']],
            "imageL": [raw['data'][(i - 1)]['images']['large']],
            "tri_up": [raw['data'][(i - 1)]['images']['triangle_down']],
            "tri_down": [raw['data'][(i - 1)]['images']['triangle_up']],
            "ranking_in_tier": [raw['data'][(i - 1)]['ranking_in_tier']],
            "mmr_change": [raw['data'][(i - 1)]['mmr_change_to_last_game']],
            "elo": [raw['data'][(i - 1)]['elo']]
        }
    return getMMRHistoryDict


ans6 = getMMRHistory("eu", "59d0eb3c-f800-5840-b043-e0eb26e76ffd")
# ans6 = getMMRHistory("eu", "b2e04f60-68e6-560c-870f-719d47ffaf9d")
pp = pprint.PrettyPrinter(sort_dicts=False)
pp.pprint(ans6)
