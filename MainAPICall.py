# pprint is used when outputting dictionaries when testing and working on the program
import pprint
# these modules allow the program to request data from the API and then parsing into a JSON file
import json
import requests
from mainGUI import popup

pp = pprint.PrettyPrinter(sort_dicts=False)


def errorCheck(status, function):
    """This function is responsible for reading the status codes when requesting data from the API"""
    if status == 400:
        popup("Request Error (missing query)." + function)
    elif status == 403:
        popup("Forbidden to connect to Riot API (mainly maintenance and side patches)." + function)
    elif status == 404:
        popup("The requested entity was not found." + function)
    elif status == 408:
        popup("Timeout while fetching data." + function)
    elif status == 429:
        popup("Rate limit reached" + function)
    elif status == 503:
        popup("Riot API seems to be down, API unable to connect." + function)
    elif status == 200:
        print("API OK")
    else:
        popup("Unknown Error" + function + "Please try again later")


# the majority or the following functions have very similar structure
# they request data from the API using specific URL generated from the users input and then store the
# result in a dictionary
# PUUID means Player Universally Unique Identifier. This is used once the original account data has been
# queried and PUUIDS do not change and are unique to the player


def getAccount(ID, tagline):
    """This function requests the most basic data liked to your RIOT account by taking 2 params ID and tagline
    and returning getAccountDict containing all the data"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "getAccount"
    # to pinpoint the error to this specific function
    errorCheck(status, "getAccount")

    # assigns values using raw dictionary
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
    """This function requests your current ranked rating by taking the region your account
    is in and your puuid (Player Universally Unique Identifier)
    and returning getMMRDataDict containing all the data"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/{region}/{puuid}')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "getMMRData"
    # to pinpoint the error to this specific function
    errorCheck(status, "getMMRData")

    # assigns values using raw dictionary
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
    """This function requests your ranked rating history by taking the region your account
    is in and your puuid and returning getMMRHistoryDict containing all the data"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr-history/{region}/{puuid}?filter=competitive')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "getMMRHistory"
    # to pinpoint the error to this specific function
    errorCheck(status, "getMMRHistory")

    # initialises dictionary and specifies all keys
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

    # iterates through the raw dictionary to assign values
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
    """This function requests the current version of the game by taking the region your account
    is in and returns regionVersionDict"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/version/{region}')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "regionVersion"
    # to pinpoint the error to this specific function
    errorCheck(status, "regionVersion")

    # assigns values using raw dictionary
    regionVersionDict = {
        1: {
            "status": [raw['status']],
            "version": [raw['data']['version']]
        }
    }
    return regionVersionDict


def getLeaderboard(region, number):
    """This function requests the current version of the leaderboard by taking the region your account
        is in and the number of player you would like to request and returns leaderboardDict"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "getLeaderboard"
    # to pinpoint the error to this specific function
    errorCheck(status, "getLeaderboard")

    # initialises dictionary and specifies all keys
    leaderboardDict = {
        0: {
            "Name": ["test"],
            "Tag": ["123"],
            "Wins": ["---"]
        }
    }

    # iterates through the raw dictionary to assign values
    for i in range(1, (number + 1)):
        leaderboardDict[i] = {
            "Name": [raw[(i - 1)]['gameName']],
            "Tag": [raw[(i - 1)]['tagLine']],
            "Wins": [raw[(i - 1)]['numberOfWins']]
        }
    return leaderboardDict


def matchID(region, puuid):
    """This function requests a short history for Match IDs for your last 3 matches of the game by taking the region
     your account is in and your puuid. It returns matchIDDict"""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?filter=competitive')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "matchID"
    # to pinpoint the error to this specific function
    errorCheck(status, "matchID")

    # initialises dictionary and specifies all keys
    matchIDDict = {
        0: {
            "match_id": ["---"],
        }
    }

    # iterates through the raw dictionary to assign values
    for i in range(1, 4):
        matchIDDict[i] = {
            "match_id": [raw['data'][(i - 1)]['metadata']['matchid']],
        }
    return matchIDDict


def matchHistory(matchid):
    """This function is the largest of its type and is responsible for fetching all the data
     to do with a particular match. The function uses a match ID as a parameter, and it returns
     two different dictionaries "matchHistoryMetadataDict" for all the non-player based data and
     "matchHistoryPlayerDataDict" for all player related data."""
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    # this requests the status code of the API
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # passes the status of the API to be checked by the errorCheck() function along with the parameter "matchHistory"
    # to pinpoint the error to this specific function
    errorCheck(status, "matchHistory")

    # initialises dictionary and specifies all keys
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

    # assigns values using raw dictionary
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

    # initialises dictionary and specifies all keys
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

    # iterates through the raw dictionary to assign values
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
    """This is the main function that is called when all data is needed by the user.
    It means that the API is just requested once rather that multiple times throughout the program. This leads to
    a slightly longer load time when the function is called but prevents errors when requesting multiple times.
    It takes the account name and its ID tag as parameters"""
    getAccountOut = getAccount(name, id)
    getMMRDataOut = getMMRData(getAccountOut['region'][0], getAccountOut['puuid'][0])
    getMMRHistoryOut = getMMRHistory(getAccountOut['region'][0], getAccountOut['puuid'][0])
    regionVersionOut = regionVersion(getAccountOut['region'][0])
    matchIDOut = matchID(getAccountOut['region'][0], getAccountOut['puuid'][0])
    matchHistoryOut = matchHistory(matchIDOut[1]['match_id'][0])

    return getAccountOut, getMMRDataOut, getMMRHistoryOut, regionVersionOut, matchIDOut, matchHistoryOut


def format_rr(rr):
    """This function does not request any data , instead formats an array of length n given in the parameter rr.
    It re-formats the array to add a + in-front of non-negative values. eg. [-21, 17, 12] ---> ['-21', '+17', '+12']"""
    main = []
    str_rr = []

    # converts all indexes to string and appends them to the new array str_rr
    for i in range(0, len(rr)):
        temp = str(rr[i])
        str_rr.append(temp)

    # iterates through the array and splits each index into its individual characters
    for x in range(0, len(str_rr)):
        split = [*(str_rr[x])]

        # if the first character is not - then a + is added and the index reconstructed and added into the new array
        if split[0] != "-":
            split.insert(0, "+")
            appended_item = "".join(split)
            main.append(appended_item)
        else:
            # if the first character is negative then nothing needs to be changed.
            # The index is reconstructed and added to the final array.
            appended_item = "".join(split)
            main.append(appended_item)
    return main
