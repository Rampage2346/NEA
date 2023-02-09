import pprint
import json
import requests

pp = pprint.PrettyPrinter(sort_dicts=False)


def errorCheck(status, function):
    if status == 400:
        print("Request Error (missing query)." + function)
    elif status == 403:
        print("Forbidden to connect to Riot API (mainly maintenance and side patches)." + function)
    elif status == 404:
        print("The requested entity was not found." + function)
    elif status == 408:
        print("Timeout while fetching data." + function)
    elif status == 429:
        print("Rate limit reached" + function)
    elif status == 503:
        print("Riot API seems to be down, API unable to connect." + function)
    else:
        print("API fully operational." + function)


def getAccount(ID, tagline):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "getAccount")

    getAccountDict = {
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
    return getAccountDict


def getMMRData(region, puuid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/{region}/{puuid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "getMMRData")

    getMMRDataDict = {
        'current_tier': [raw['data']['currenttier']],
        'current_tier_patched': [raw['data']['currenttierpatched']],
        'imageS': [raw['data']['images']['small']],
        'imageL': [raw['data']['images']['large']],
        'tri_up': [raw['data']['images']['triangle_up']],
        'tri_down': [raw['data']['images']['triangle_down']],
        'ranking_in_tier': [raw['data']['ranking_in_tier']],
        'mmr_change': [raw['data']['mmr_change_to_last_game']],
        'elo': [raw['data']['elo']],
    }
    return getMMRDataDict


def getMMRHistory(region, puuid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr-history/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "getMMRHistory")

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

    for i in range(1, 5):
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


def regionVersion(region):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/version/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "regionVersion")

    regionVersionDict = {
        1: {
            "status": [raw['status']],
            "version": [raw['data']['version']]
        }
    }
    return regionVersionDict


def getLeaderboard(region, number):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "getLeaderboard")

    leaderboardDict = {
        0: {
            "Name": ["test"],
            "Tag": ["123"],
            "Wins": ["---"]
        }
    }

    for i in range(1, (number + 1)):
        leaderboardDict[i] = {
            "Name": [raw[(i - 1)]['gameName']],
            "Tag": [raw[(i - 1)]['tagLine']],
            "Wins": [raw[(i - 1)]['numberOfWins']]
        }
    return leaderboardDict


def matchID(region, puuid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "matchID")

    matchIDDict = {
        0: {
            "match_id": ["---"],
        }
    }

    for i in range(1, 2):
        matchIDDict[i] = {
            "match_id": [raw['data'][(i - 1)]['metadata']['matchid']],
        }
    return matchIDDict


def matchHistory(matchid):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    errorCheck(status, "matchHistory")

    matchHistoryMetadataDict = {
        0: {
            "map": ["---"],
            "game_start_patched": ["---"],
            "rounds_played": ["---"],
            "mode": ["---"],
            "queue": ["---"],
            "region": ["---"],
            "cluster": ["---"]
        }
    }

    matchHistoryMetadataDict = {
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

    matchHistoryPlayerDataDict = {
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
        matchHistoryPlayerDataDict[i] = {
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

    return matchHistoryMetadataDict, matchHistoryPlayerDataDict


def allPlayerData(name, id):
    getAccountOut = getAccount(name, id)
    getMMRDataOut = getMMRData(getAccountOut['region'][0], getAccountOut['puuid'][0])
    getMMRHistoryOut = getMMRHistory(getAccountOut['region'][0], getAccountOut['puuid'][0])
    regionVersionOut = regionVersion(getAccountOut['region'][0])
    matchIDOut = matchID(getAccountOut['region'][0], getAccountOut['puuid'][0])
    matchHistoryOut = matchHistory(matchIDOut[1]['match_id'][0])

    return getAccountOut, getMMRDataOut, getMMRHistoryOut, regionVersionOut, matchIDOut, matchHistoryOut


# a = allPlayerData("Amaz", "4510")
# pp.pprint(a[0])
# pp.pprint(a[1])
# pp.pprint(a[2])
# pp.pprint(a[3])
# pp.pprint(a[4])
# pp.pprint(a[5])
