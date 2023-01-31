import pprint
import json
import requests


def getAccount(ID, tagline):
    global puuid, region, accountlvl, name, tag, cardS, cardL, cardW, cardID

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # all current account details
    puuid = raw['data']['puuid']
    region = raw['data']['region']
    accountlvl = raw['data']['account_level']
    name = raw['data']['name']
    tag = raw['data']['tag']
    cardS = raw['data']['card']['small']
    cardL = raw['data']['card']['large']
    cardW = raw['data']['card']['wide']
    cardID = raw['data']['card']['id']


def getMMRData(region, puuid):
    global current_tier, current_tier_patched, imageS, imageL, tri_up, tri_down, ranking_in_tier, mmr_change, elo

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/{region}/{puuid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # fetches all current MMR data
    current_tier = raw['data']['currenttier']
    current_tier_patched = raw['data']['currenttierpatched']
    imageS = raw['data']['images']['small']
    imageL = raw['data']['images']['large']
    tri_up = raw['data']['images']['triangle_down']
    tri_down = raw['data']['images']['triangle_up']
    ranking_in_tier = raw['data']['ranking_in_tier']
    mmr_change = raw['data']['mmr_change_to_last_game']
    elo = raw['data']['elo']


def getMMRHistory(region, puuid):
    global current_tierm1, imageSm1, imageLm1, tri_upm1, tri_downm1, ranking_in_tierm1, mmr_changem1
    global current_tierm2, imageSm2, imageLm2, tri_upm2, tri_downm2, ranking_in_tierm2, mmr_changem2
    global current_tierm3, imageSm3, imageLm3, tri_upm3, tri_downm3, ranking_in_tierm3, mmr_changem3
    global current_tierm4, imageSm4, imageLm4, tri_upm4, tri_downm4, ranking_in_tierm4, mmr_changem4
    global current_tierm5, imageSm5, imageLm5, tri_upm5, tri_downm5, ranking_in_tierm5, mmr_changem5

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr-history/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # match1
    current_tierm1 = raw['data'][0]['currenttierpatched']
    imageSm1 = raw['data'][0]['images']['small']
    imageLm1 = raw['data'][0]['images']['large']
    tri_upm1 = raw['data'][0]['images']['triangle_down']
    tri_downm1 = raw['data'][0]['images']['triangle_up']
    ranking_in_tierm1 = raw['data'][0]['ranking_in_tier']
    mmr_changem1 = raw['data'][0]['mmr_change_to_last_game']
    elom1 = raw['data'][0]['elo']

    # match2
    current_tierm2 = raw['data'][1]['currenttierpatched']
    imageSm2 = raw['data'][1]['images']['small']
    imageLm2 = raw['data'][1]['images']['large']
    tri_upm2 = raw['data'][1]['images']['triangle_down']
    tri_downm2 = raw['data'][1]['images']['triangle_up']
    ranking_in_tierm2 = raw['data'][1]['ranking_in_tier']
    mmr_changem2 = raw['data'][1]['mmr_change_to_last_game']
    elom2 = raw['data'][1]['elo']

    # match3
    current_tierm3 = raw['data'][2]['currenttierpatched']
    imageSm3 = raw['data'][2]['images']['small']
    imageLm3 = raw['data'][2]['images']['large']
    tri_upm3 = raw['data'][2]['images']['triangle_down']
    tri_downm3 = raw['data'][2]['images']['triangle_up']
    ranking_in_tierm3 = raw['data'][2]['ranking_in_tier']
    mmr_changem3 = raw['data'][2]['mmr_change_to_last_game']
    elom3 = raw['data'][2]['elo']

    # match4
    current_tierm4 = raw['data'][3]['currenttierpatched']
    imageSm4 = raw['data'][3]['images']['small']
    imageLm4 = raw['data'][3]['images']['large']
    tri_upm4 = raw['data'][3]['images']['triangle_down']
    tri_downm4 = raw['data'][3]['images']['triangle_up']
    ranking_in_tierm4 = raw['data'][3]['ranking_in_tier']
    mmr_changem4 = raw['data'][3]['mmr_change_to_last_game']
    elom4 = raw['data'][3]['elo']

    # match5
    current_tierm5 = raw['data'][4]['currenttierpatched']
    imageSm5 = raw['data'][4]['images']['small']
    imageLm5 = raw['data'][4]['images']['large']
    tri_upm5 = raw['data'][4]['images']['triangle_down']
    tri_downm5 = raw['data'][4]['images']['triangle_up']
    ranking_in_tierm5 = raw['data'][4]['ranking_in_tier']
    mmr_changem5 = raw['data'][4]['mmr_change_to_last_game']
    elom5 = raw['data'][4]['elo']


def matchID(region, puuid):
    global matchID1, matchID2, matchID3, matchID4, matchID5

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?filter=competitive')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    # fetches match ID from last 5 games
    matchID1 = raw['data'][0]['metadata']['matchid']
    matchID2 = raw['data'][1]['metadata']['matchid']
    matchID3 = raw['data'][2]['metadata']['matchid']
    matchID4 = raw['data'][3]['metadata']['matchid']
    matchID5 = raw['data'][4]['metadata']['matchid']


def matchHistoryPlayer1(matchid):
    global ccasts1, ecasts1, qcasts1, xcasts1, agent_bust1, agent_full1, agent_kill_feed1, agent_small1, character1, current_tier1
    global damage_made1, damage_received1, loadout_avg1, loadout_overall1, spent_avg1, spent_overall1
    global assists1, bodyshots1, deaths1, headshots1, kills1, legshots1, score1, team1

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts1 = raw['data']['players']['all_players'][0]['ability_casts']['c_cast']
    ecasts1 = raw['data']['players']['all_players'][0]['ability_casts']['e_cast']
    qcasts1 = raw['data']['players']['all_players'][0]['ability_casts']['q_cast']
    xcasts1 = raw['data']['players']['all_players'][0]['ability_casts']['x_cast']

    agent_bust1 = raw['data']['players']['all_players'][0]['assets']['agent']['bust']
    agent_full1 = raw['data']['players']['all_players'][0]['assets']['agent']['full']
    agent_kill_feed1 = raw['data']['players']['all_players'][0]['assets']['agent']['killfeed']
    agent_small1 = raw['data']['players']['all_players'][0]['assets']['agent']['small']

    character1 = raw['data']['players']['all_players'][0]['character']
    current_tier1 = raw['data']['players']['all_players'][0]['currenttier_patched']

    damage_made1 = raw['data']['players']['all_players'][0]['damage_made']
    damage_received1 = raw['data']['players']['all_players'][0]['damage_received']

    loadout_avg1 = raw['data']['players']['all_players'][0]['economy']['loadout_value']['average']
    loadout_overall1 = raw['data']['players']['all_players'][0]['economy']['loadout_value']['overall']
    spent_avg1 = raw['data']['players']['all_players'][0]['economy']['spent']['average']
    spent_overall1 = raw['data']['players']['all_players'][0]['economy']['spent']['overall']

    assists1 = raw['data']['players']['all_players'][0]['stats']['assists']
    bodyshots1 = raw['data']['players']['all_players'][0]['stats']['bodyshots']
    deaths1 = raw['data']['players']['all_players'][0]['stats']['deaths']
    headshots1 = raw['data']['players']['all_players'][0]['stats']['headshots']
    kills1 = raw['data']['players']['all_players'][0]['stats']['kills']
    legshots1 = raw['data']['players']['all_players'][0]['stats']['legshots']
    score1 = raw['data']['players']['all_players'][0]['stats']['score']

    team1 = raw['data']['players']['all_players'][0]['team']


def matchHistoryPlayer2(matchid):
    global ccasts2, ecasts2, qcasts2, xcasts2, agent_bust2, agent_full2, agent_kill_feed2, agent_small2, character2, current_tier2
    global damage_made2, damage_received2, loadout_avg2, loadout_overall2, spent_avg2, spent_overall2
    global assists2, bodyshots2, deaths2, headshots2, kills2, legshots2, score2, team2

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts2 = raw['data']['players']['all_players'][1]['ability_casts']['c_cast']
    ecasts2 = raw['data']['players']['all_players'][1]['ability_casts']['e_cast']
    qcasts2 = raw['data']['players']['all_players'][1]['ability_casts']['q_cast']
    xcasts2 = raw['data']['players']['all_players'][1]['ability_casts']['x_cast']

    agent_bust2 = raw['data']['players']['all_players'][1]['assets']['agent']['bust']
    agent_full2 = raw['data']['players']['all_players'][1]['assets']['agent']['full']
    agent_kill_feed2 = raw['data']['players']['all_players'][1]['assets']['agent']['killfeed']
    agent_small2 = raw['data']['players']['all_players'][1]['assets']['agent']['small']

    character2 = raw['data']['players']['all_players'][1]['character']
    current_tier2 = raw['data']['players']['all_players'][1]['currenttier_patched']

    damage_made2 = raw['data']['players']['all_players'][1]['damage_made']
    damage_received2 = raw['data']['players']['all_players'][1]['damage_received']

    loadout_avg2 = raw['data']['players']['all_players'][1]['economy']['loadout_value']['average']
    loadout_overall2 = raw['data']['players']['all_players'][1]['economy']['loadout_value']['overall']
    spent_avg2 = raw['data']['players']['all_players'][1]['economy']['spent']['average']
    spent_overall2 = raw['data']['players']['all_players'][1]['economy']['spent']['overall']

    assists2 = raw['data']['players']['all_players'][1]['stats']['assists']
    bodyshots2 = raw['data']['players']['all_players'][1]['stats']['bodyshots']
    deaths2 = raw['data']['players']['all_players'][1]['stats']['deaths']
    headshots2 = raw['data']['players']['all_players'][1]['stats']['headshots']
    kills2 = raw['data']['players']['all_players'][1]['stats']['kills']
    legshots2 = raw['data']['players']['all_players'][1]['stats']['legshots']
    score2 = raw['data']['players']['all_players'][1]['stats']['score']

    team2 = raw['data']['players']['all_players'][1]['team']


def matchHistoryPlayer3(matchid):
    global ccasts3, ecasts3, qcasts3, xcasts3, agent_bust3, agent_full3, agent_kill_feed3, agent_small3, character3, current_tier3
    global damage_made3, damage_received3, loadout_avg3, loadout_overall3, spent_avg3, spent_overall3
    global assists3, bodyshots3, deaths3, headshots3, kills3, legshots3, score3, team3

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts3 = raw['data']['players']['all_players'][2]['ability_casts']['c_cast']
    ecasts3 = raw['data']['players']['all_players'][2]['ability_casts']['e_cast']
    qcasts3 = raw['data']['players']['all_players'][2]['ability_casts']['q_cast']
    xcasts3 = raw['data']['players']['all_players'][2]['ability_casts']['x_cast']

    agent_bust3 = raw['data']['players']['all_players'][2]['assets']['agent']['bust']
    agent_full3 = raw['data']['players']['all_players'][2]['assets']['agent']['full']
    agent_kill_feed3 = raw['data']['players']['all_players'][2]['assets']['agent']['killfeed']
    agent_small3 = raw['data']['players']['all_players'][2]['assets']['agent']['small']

    character3 = raw['data']['players']['all_players'][2]['character']
    current_tier3 = raw['data']['players']['all_players'][2]['currenttier_patched']

    damage_made3 = raw['data']['players']['all_players'][2]['damage_made']
    damage_received3 = raw['data']['players']['all_players'][2]['damage_received']

    loadout_avg3 = raw['data']['players']['all_players'][2]['economy']['loadout_value']['average']
    loadout_overall3 = raw['data']['players']['all_players'][2]['economy']['loadout_value']['overall']
    spent_avg3 = raw['data']['players']['all_players'][2]['economy']['spent']['average']
    spent_overall3 = raw['data']['players']['all_players'][2]['economy']['spent']['overall']

    assists3 = raw['data']['players']['all_players'][2]['stats']['assists']
    bodyshots3 = raw['data']['players']['all_players'][2]['stats']['bodyshots']
    deaths3 = raw['data']['players']['all_players'][2]['stats']['deaths']
    headshots3 = raw['data']['players']['all_players'][2]['stats']['headshots']
    kills3 = raw['data']['players']['all_players'][2]['stats']['kills']
    legshots3 = raw['data']['players']['all_players'][2]['stats']['legshots']
    score3 = raw['data']['players']['all_players'][2]['stats']['score']

    team3 = raw['data']['players']['all_players'][2]['team']


def matchHistoryPlayer4(matchid):
    global ccasts4, ecasts4, qcasts4, xcasts4, agent_bust4, agent_full4, agent_kill_feed4, agent_small4, character4, current_tier4
    global damage_made4, damage_received4, loadout_avg4, loadout_overall4, spent_avg4, spent_overall4
    global assists4, bodyshots4, deaths4, headshots4, kills4, legshots4, score4, team4

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts4 = raw['data']['players']['all_players'][3]['ability_casts']['c_cast']
    ecasts4 = raw['data']['players']['all_players'][3]['ability_casts']['e_cast']
    qcasts4 = raw['data']['players']['all_players'][3]['ability_casts']['q_cast']
    xcasts4 = raw['data']['players']['all_players'][3]['ability_casts']['x_cast']

    agent_bust4 = raw['data']['players']['all_players'][3]['assets']['agent']['bust']
    agent_full4 = raw['data']['players']['all_players'][3]['assets']['agent']['full']
    agent_kill_feed4 = raw['data']['players']['all_players'][3]['assets']['agent']['killfeed']
    agent_small4 = raw['data']['players']['all_players'][3]['assets']['agent']['small']

    character4 = raw['data']['players']['all_players'][3]['character']
    current_tier4 = raw['data']['players']['all_players'][3]['currenttier_patched']

    damage_made4 = raw['data']['players']['all_players'][3]['damage_made']
    damage_received4 = raw['data']['players']['all_players'][3]['damage_received']

    loadout_avg4 = raw['data']['players']['all_players'][3]['economy']['loadout_value']['average']
    loadout_overall4 = raw['data']['players']['all_players'][3]['economy']['loadout_value']['overall']
    spent_avg4 = raw['data']['players']['all_players'][3]['economy']['spent']['average']
    spent_overall4 = raw['data']['players']['all_players'][3]['economy']['spent']['overall']

    assists4 = raw['data']['players']['all_players'][3]['stats']['assists']
    bodyshots4 = raw['data']['players']['all_players'][3]['stats']['bodyshots']
    deaths4 = raw['data']['players']['all_players'][3]['stats']['deaths']
    headshots4 = raw['data']['players']['all_players'][3]['stats']['headshots']
    kills4 = raw['data']['players']['all_players'][3]['stats']['kills']
    legshots4 = raw['data']['players']['all_players'][3]['stats']['legshots']
    score4 = raw['data']['players']['all_players'][3]['stats']['score']

    team4 = raw['data']['players']['all_players'][3]['team']


def matchHistoryPlayer5(matchid):
    global ccasts5, ecasts5, qcasts5, xcasts5, agent_bust5, agent_full5, agent_kill_feed5, agent_small5, character5, current_tier5
    global damage_made5, damage_received5, loadout_avg5, loadout_overall5, spent_avg5, spent_overall5
    global assists5, bodyshots5, deaths5, headshots5, kills5, legshots5, score5, team5

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts5 = raw['data']['players']['all_players'][4]['ability_casts']['c_cast']
    ecasts5 = raw['data']['players']['all_players'][4]['ability_casts']['e_cast']
    qcasts5 = raw['data']['players']['all_players'][4]['ability_casts']['q_cast']
    xcasts5 = raw['data']['players']['all_players'][4]['ability_casts']['x_cast']

    agent_bust5 = raw['data']['players']['all_players'][4]['assets']['agent']['bust']
    agent_full5 = raw['data']['players']['all_players'][4]['assets']['agent']['full']
    agent_kill_feed5 = raw['data']['players']['all_players'][4]['assets']['agent']['killfeed']
    agent_small5 = raw['data']['players']['all_players'][4]['assets']['agent']['small']

    character5 = raw['data']['players']['all_players'][4]['character']
    current_tier5 = raw['data']['players']['all_players'][4]['currenttier_patched']

    damage_made5 = raw['data']['players']['all_players'][4]['damage_made']
    damage_received5 = raw['data']['players']['all_players'][4]['damage_received']

    loadout_avg5 = raw['data']['players']['all_players'][4]['economy']['loadout_value']['average']
    loadout_overall5 = raw['data']['players']['all_players'][4]['economy']['loadout_value']['overall']
    spent_avg5 = raw['data']['players']['all_players'][4]['economy']['spent']['average']
    spent_overall5 = raw['data']['players']['all_players'][4]['economy']['spent']['overall']

    assists5 = raw['data']['players']['all_players'][4]['stats']['assists']
    bodyshots5 = raw['data']['players']['all_players'][4]['stats']['bodyshots']
    deaths5 = raw['data']['players']['all_players'][4]['stats']['deaths']
    headshots5 = raw['data']['players']['all_players'][4]['stats']['headshots']
    kills5 = raw['data']['players']['all_players'][4]['stats']['kills']
    legshots5 = raw['data']['players']['all_players'][4]['stats']['legshots']
    score5 = raw['data']['players']['all_players'][4]['stats']['score']

    team5 = raw['data']['players']['all_players'][4]['team']


def matchHistoryPlayer6(matchid):
    global ccasts6, ecasts6, qcasts6, xcasts6, agent_bust6, agent_full6, agent_kill_feed6, agent_small6, character6, current_tier6
    global damage_made6, damage_received6, loadout_avg6, loadout_overall6, spent_avg6, spent_overall6
    global assists6, bodyshots6, deaths6, headshots6, kills6, legshots6, score6, team6

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts6 = raw['data']['players']['all_players'][5]['ability_casts']['c_cast']
    ecasts6 = raw['data']['players']['all_players'][5]['ability_casts']['e_cast']
    qcasts6 = raw['data']['players']['all_players'][5]['ability_casts']['q_cast']
    xcasts6 = raw['data']['players']['all_players'][5]['ability_casts']['x_cast']

    agent_bust6 = raw['data']['players']['all_players'][5]['assets']['agent']['bust']
    agent_full6 = raw['data']['players']['all_players'][5]['assets']['agent']['full']
    agent_kill_feed6 = raw['data']['players']['all_players'][5]['assets']['agent']['killfeed']
    agent_small6 = raw['data']['players']['all_players'][5]['assets']['agent']['small']

    character6 = raw['data']['players']['all_players'][5]['character']
    current_tier6 = raw['data']['players']['all_players'][5]['currenttier_patched']

    damage_made6 = raw['data']['players']['all_players'][5]['damage_made']
    damage_received6 = raw['data']['players']['all_players'][5]['damage_received']

    loadout_avg6 = raw['data']['players']['all_players'][5]['economy']['loadout_value']['average']
    loadout_overall6 = raw['data']['players']['all_players'][5]['economy']['loadout_value']['overall']
    spent_avg6 = raw['data']['players']['all_players'][5]['economy']['spent']['average']
    spent_overall6 = raw['data']['players']['all_players'][5]['economy']['spent']['overall']

    assists6 = raw['data']['players']['all_players'][5]['stats']['assists']
    bodyshots6 = raw['data']['players']['all_players'][5]['stats']['bodyshots']
    deaths6 = raw['data']['players']['all_players'][5]['stats']['deaths']
    headshots6 = raw['data']['players']['all_players'][5]['stats']['headshots']
    kills6 = raw['data']['players']['all_players'][5]['stats']['kills']
    legshots6 = raw['data']['players']['all_players'][5]['stats']['legshots']
    score6 = raw['data']['players']['all_players'][5]['stats']['score']

    team6 = raw['data']['players']['all_players'][5]['team']


def matchHistoryPlayer7(matchid):
    global ccasts7, ecasts7, qcasts7, xcasts7, agent_bust7, agent_full7, agent_kill_feed7, agent_small7, character7, current_tier7
    global damage_made7, damage_received7, loadout_avg7, loadout_overall7, spent_avg7, spent_overall7
    global assists7, bodyshots7, deaths7, headshots7, kills7, legshots7, score7, team7

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts7 = raw['data']['players']['all_players'][6]['ability_casts']['c_cast']
    ecasts7 = raw['data']['players']['all_players'][6]['ability_casts']['e_cast']
    qcasts7 = raw['data']['players']['all_players'][6]['ability_casts']['q_cast']
    xcasts7 = raw['data']['players']['all_players'][6]['ability_casts']['x_cast']

    agent_bust7 = raw['data']['players']['all_players'][6]['assets']['agent']['bust']
    agent_full7 = raw['data']['players']['all_players'][6]['assets']['agent']['full']
    agent_kill_feed7 = raw['data']['players']['all_players'][6]['assets']['agent']['killfeed']
    agent_small7 = raw['data']['players']['all_players'][6]['assets']['agent']['small']

    character7 = raw['data']['players']['all_players'][6]['character']
    current_tier7 = raw['data']['players']['all_players'][6]['currenttier_patched']

    damage_made7 = raw['data']['players']['all_players'][6]['damage_made']
    damage_received7 = raw['data']['players']['all_players'][6]['damage_received']

    loadout_avg7 = raw['data']['players']['all_players'][6]['economy']['loadout_value']['average']
    loadout_overall7 = raw['data']['players']['all_players'][6]['economy']['loadout_value']['overall']
    spent_avg7 = raw['data']['players']['all_players'][6]['economy']['spent']['average']
    spent_overall7 = raw['data']['players']['all_players'][6]['economy']['spent']['overall']

    assists7 = raw['data']['players']['all_players'][6]['stats']['assists']
    bodyshots7 = raw['data']['players']['all_players'][6]['stats']['bodyshots']
    deaths7 = raw['data']['players']['all_players'][6]['stats']['deaths']
    headshots7 = raw['data']['players']['all_players'][6]['stats']['headshots']
    kills7 = raw['data']['players']['all_players'][6]['stats']['kills']
    legshots7 = raw['data']['players']['all_players'][6]['stats']['legshots']
    score7 = raw['data']['players']['all_players'][6]['stats']['score']

    team7 = raw['data']['players']['all_players'][6]['team']


def matchHistoryPlayer8(matchid):
    global ccasts8, ecasts8, qcasts8, xcasts8, agent_bust8, agent_full8, agent_kill_feed8, agent_small8, character8, current_tier8
    global damage_made8, damage_received8, loadout_avg8, loadout_overall8, spent_avg8, spent_overall8
    global assists8, bodyshots8, deaths8, headshots8, kills8, legshots8, score8, team8

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts8 = raw['data']['players']['all_players'][7]['ability_casts']['c_cast']
    ecasts8 = raw['data']['players']['all_players'][7]['ability_casts']['e_cast']
    qcasts8 = raw['data']['players']['all_players'][7]['ability_casts']['q_cast']
    xcasts8 = raw['data']['players']['all_players'][7]['ability_casts']['x_cast']

    agent_bust8 = raw['data']['players']['all_players'][7]['assets']['agent']['bust']
    agent_full8 = raw['data']['players']['all_players'][7]['assets']['agent']['full']
    agent_kill_feed8 = raw['data']['players']['all_players'][7]['assets']['agent']['killfeed']
    agent_small8 = raw['data']['players']['all_players'][7]['assets']['agent']['small']

    character8 = raw['data']['players']['all_players'][7]['character']
    current_tier8 = raw['data']['players']['all_players'][7]['currenttier_patched']

    damage_made8 = raw['data']['players']['all_players'][7]['damage_made']
    damage_received8 = raw['data']['players']['all_players'][7]['damage_received']

    loadout_avg8 = raw['data']['players']['all_players'][7]['economy']['loadout_value']['average']
    loadout_overall8 = raw['data']['players']['all_players'][7]['economy']['loadout_value']['overall']
    spent_avg8 = raw['data']['players']['all_players'][7]['economy']['spent']['average']
    spent_overall8 = raw['data']['players']['all_players'][7]['economy']['spent']['overall']

    assists8 = raw['data']['players']['all_players'][7]['stats']['assists']
    bodyshots8 = raw['data']['players']['all_players'][7]['stats']['bodyshots']
    deaths8 = raw['data']['players']['all_players'][7]['stats']['deaths']
    headshots8 = raw['data']['players']['all_players'][7]['stats']['headshots']
    kills8 = raw['data']['players']['all_players'][7]['stats']['kills']
    legshots8 = raw['data']['players']['all_players'][7]['stats']['legshots']
    score8 = raw['data']['players']['all_players'][7]['stats']['score']

    team8 = raw['data']['players']['all_players'][7]['team']


def matchHistoryPlayer9(matchid):
    global ccasts9, ecasts9, qcasts9, xcasts9, agent_bust9, agent_full9, agent_kill_feed9, agent_small9, character9, current_tier9
    global damage_made9, damage_received9, loadout_avg9, loadout_overall9, spent_avg9, spent_overall9
    global assists9, bodyshots9, deaths9, headshots9, kills9, legshots9, score9, team9

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts9 = raw['data']['players']['all_players'][8]['ability_casts']['c_cast']
    ecasts9 = raw['data']['players']['all_players'][8]['ability_casts']['e_cast']
    qcasts9 = raw['data']['players']['all_players'][8]['ability_casts']['q_cast']
    xcasts9 = raw['data']['players']['all_players'][8]['ability_casts']['x_cast']

    agent_bust9 = raw['data']['players']['all_players'][8]['assets']['agent']['bust']
    agent_full9 = raw['data']['players']['all_players'][8]['assets']['agent']['full']
    agent_kill_feed9 = raw['data']['players']['all_players'][8]['assets']['agent']['killfeed']
    agent_small9 = raw['data']['players']['all_players'][8]['assets']['agent']['small']

    character9 = raw['data']['players']['all_players'][8]['character']
    current_tier9 = raw['data']['players']['all_players'][8]['currenttier_patched']

    damage_made9 = raw['data']['players']['all_players'][8]['damage_made']
    damage_received9 = raw['data']['players']['all_players'][8]['damage_received']

    loadout_avg9 = raw['data']['players']['all_players'][8]['economy']['loadout_value']['average']
    loadout_overall9 = raw['data']['players']['all_players'][8]['economy']['loadout_value']['overall']
    spent_avg9 = raw['data']['players']['all_players'][8]['economy']['spent']['average']
    spent_overall9 = raw['data']['players']['all_players'][8]['economy']['spent']['overall']

    assists9 = raw['data']['players']['all_players'][8]['stats']['assists']
    bodyshots9 = raw['data']['players']['all_players'][8]['stats']['bodyshots']
    deaths9 = raw['data']['players']['all_players'][8]['stats']['deaths']
    headshots9 = raw['data']['players']['all_players'][8]['stats']['headshots']
    kills9 = raw['data']['players']['all_players'][8]['stats']['kills']
    legshots9 = raw['data']['players']['all_players'][8]['stats']['legshots']
    score9 = raw['data']['players']['all_players'][8]['stats']['score']

    team9 = raw['data']['players']['all_players'][8]['team']


def matchHistoryPlayer10(matchid):
    global ccasts10, ecasts10, qcasts10, xcasts10, agent_bust10, agent_full10, agent_kill_feed10, agent_small10, character10, current_tier10
    global damage_made10, damage_received10, loadout_avg10, loadout_overall10, spent_avg10, spent_overall10
    global assists10, bodyshots10, deaths10, headshots10, kills10, legshots10, score10, team10

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v2/match/{matchid}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    ccasts10 = raw['data']['players']['all_players'][9]['ability_casts']['c_cast']
    ecasts10 = raw['data']['players']['all_players'][9]['ability_casts']['e_cast']
    qcasts10 = raw['data']['players']['all_players'][9]['ability_casts']['q_cast']
    xcasts10 = raw['data']['players']['all_players'][9]['ability_casts']['x_cast']

    agent_bust10 = raw['data']['players']['all_players'][9]['assets']['agent']['bust']
    agent_full10 = raw['data']['players']['all_players'][9]['assets']['agent']['full']
    agent_kill_feed10 = raw['data']['players']['all_players'][9]['assets']['agent']['killfeed']
    agent_small10 = raw['data']['players']['all_players'][9]['assets']['agent']['small']

    character10 = raw['data']['players']['all_players'][9]['character']
    current_tier10 = raw['data']['players']['all_players'][9]['currenttier_patched']

    damage_made10 = raw['data']['players']['all_players'][9]['damage_made']
    damage_received10 = raw['data']['players']['all_players'][9]['damage_received']

    loadout_avg10 = raw['data']['players']['all_players'][9]['economy']['loadout_value']['average']
    loadout_overall10 = raw['data']['players']['all_players'][9]['economy']['loadout_value']['overall']
    spent_avg10 = raw['data']['players']['all_players'][9]['economy']['spent']['average']
    spent_overall10 = raw['data']['players']['all_players'][9]['economy']['spent']['overall']

    assists10 = raw['data']['players']['all_players'][9]['stats']['assists']
    bodyshots10 = raw['data']['players']['all_players'][9]['stats']['bodyshots']
    deaths10 = raw['data']['players']['all_players'][9]['stats']['deaths']
    headshots10 = raw['data']['players']['all_players'][9]['stats']['headshots']
    kills10 = raw['data']['players']['all_players'][9]['stats']['kills']
    legshots10 = raw['data']['players']['all_players'][9]['stats']['legshots']
    score10 = raw['data']['players']['all_players'][9]['stats']['score']

    team10 = raw['data']['players']['all_players'][9]['team']


def regionVersion(region):
    global status, version

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/version/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    status = raw['status']
    version = raw['data']['version']




def getLeaderboard(region):
    global leaderboard

    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    leaderboard = {
        "Name": [],
        "Tag": [],
        "Rank": [],
        "Wins": []
    }

    for i in range(0, 49):
        tempname = raw[i]['gameName']
        temptag = raw[i]['tagLine']
        temprank = raw[i]['leaderboardRank']
        tempwins = raw[i]['numberOfWins']

        leaderboard["Name"].append(tempname)
        leaderboard["Tag"].append(temptag)
        leaderboard["Rank"].append(temprank)
        leaderboard["Wins"].append(tempwins)










inp1 = input("Enter your unique Riot ID:\n\t")
inp2 = input("Enter your Riot Tagline:\n\t")

getAccount(inp1, inp2)
# print(puuid, region, accountlvl, name, tag, cardS, cardL, cardW, cardID)
getMMRData(region, puuid)
# print(currenttier, currenttierpatched, imageS, imageL, tri_up, tri_down, ranking_in_tier, MMRchange, elo)
getMMRHistory(region, puuid)
# print(currenttierm1, imageSm2, imageLm3 , tri_upm4, tri_downm5, ranking_in_tierm1, mmrchangem2)
matchID(region, puuid)
# print(matchID1, matchID2, matchID3, matchID4, matchID5)
print(matchID1)
print("-----")
matchHistoryPlayer1(matchID1)
print(ccasts1, ecasts1, qcasts1, xcasts1, agent_bust1, agent_full1, agent_kill_feed1, agent_small1, character1,
      current_tier1)
print("-----")
print(damage_made1, damage_received1, loadout_avg1, loadout_overall1, spent_avg1, spent_overall1)
print("-----")
print(assists1, bodyshots1, deaths1, headshots1, kills1, legshots1, score1, team1)

matchHistoryPlayer1(matchID1)
print(ecasts1)

matchHistoryPlayer2(matchID1)
print(ecasts2)

matchHistoryPlayer3(matchID1)
print(ecasts3)

matchHistoryPlayer4(matchID1)
print(ecasts4)

matchHistoryPlayer5(matchID1)
print(ecasts5)

matchHistoryPlayer6(matchID1)
print(ecasts6)

matchHistoryPlayer7(matchID1)
print(ecasts7)

matchHistoryPlayer8(matchID1)
print(ecasts8)

matchHistoryPlayer9(matchID1)
print(ecasts9)

matchHistoryPlayer10(matchID1)
print(ecasts10)
