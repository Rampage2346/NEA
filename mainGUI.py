import PySimpleGUI as sg
import pprint
import requests
from PIL import Image
import io
from login import login_cred_check, new_user_append
from MainAPICall import allPlayerData, format_rr, getLeaderboard, matchID, matchHistory

# import time

# from options import recent_match_summary_option, leader_option, match_breakdown_option

pp = pprint.PrettyPrinter(sort_dicts=False)


def loading():
    sg.theme('DarkBlue')

    load = [
        [sg.Text('Fetching data...')]
    ]

    layout = [
        [sg.Column(load, justification='c')],
        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar', style="clam")]
    ]

    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    progress_bar = window['progressbar']
    for i in range(1000):
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
        progress_bar.UpdateBar(i + 1)
    window.close()


def popup(message):
    sg.theme('DarkBlue')
    column_to_be_centered = [
        [sg.Text(message)],
        [sg.Push(), sg.Button('OK')]
    ]

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]

    sg.Window('MetaTrak', layout, modal=True, icon='valorant.ico').read(close=True)


def login_or_adduser():
    sg.theme('DarkBlue')
    layout = [
        [sg.Canvas()],
        [sg.Canvas(), sg.Text("Please Choose an Option:"), sg.Canvas()],
        [sg.Canvas()],
        [sg.Canvas(), sg.Button("I already have an account"), sg.Button("I am a new user"), sg.Canvas()]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event = window.read()
    window.close()

    return event


def login_window():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Enter Your Username')],
        [sg.InputText()],
        [sg.Text('Enter Your Password')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()

    return event, values


def new_user_window():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Enter Your Username:')],
        [sg.InputText()],
        [sg.Text('Enter Your New Password:')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()

    return event, values


def api_login_window():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Enter Your Riot ID:')],
        [sg.InputText()],
        [sg.Text('Enter Your Tagline:')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()

    return event, values


def main_login():
    popup("Welcome To MetaTrak, a python application responsible for your imminent improvement at Valorant! \nOn the "
          "next screen you will need to login or create a new account.")

    login_choice = login_or_adduser()
    # print(login_choice)

    if login_choice[0] == "I already have an account":
        check = False
        login_inp_array = login_window()
        if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        # print(login_inp_array)
        check = login_cred_check(login_inp_array[1][0], login_inp_array[1][1])
        # print(check)
        while check is False:
            popup("Incorrect Username or Password!\nPlease try again.")
            login_inp_array = login_window()
            if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
                exit()
            # print(login_inp_array)
            check = login_cred_check(login_inp_array[1][0], login_inp_array[1][1])
            # print(check)

    elif login_choice[0] == "I am a new user":
        new_user_inp_array = new_user_window()
        if new_user_inp_array[0] == 'Cancel' or new_user_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        # print(new_user_inp_array)
        new_user_append(new_user_inp_array[1][0], new_user_inp_array[1][1])


def api_login():
    popup("You have now logged in or created your new account. Now you will need to provide the Valorant account \n"
          "that you would like to fetch the stats for. This means your IGN and your tagline, the string after the #.\n")
    api_inp_array = api_login_window()
    return api_inp_array[1][0], api_inp_array[1][1]


def main_menu():
    sg.theme('DarkBlue')

    card_bytes = requests.get(account_data["cardW"][0])
    card_image = Image.open(io.BytesIO(card_bytes.content))
    card_png = io.BytesIO()
    card_image.save(card_png, format="PNG")
    card_display = card_png.getvalue()

    rank_bytes = requests.get(mmr_data["imageS"][0])
    rank_image = Image.open(io.BytesIO(rank_bytes.content))
    rank_png = io.BytesIO()
    rank_image.save(rank_png, format="PNG")
    rank_display = rank_png.getvalue()

    name = account_data["name"][0]
    account_level = str(account_data["accountlvl"][0])
    region = (account_data["region"][0]).upper()
    current_rank = mmr_data["current_tier_patched"][0]
    ranking_in_tier = mmr_data["ranking_in_tier"][0]

    card = sg.Image(data=card_display)
    rank = sg.Image(data=rank_display)

    rank_curr = [
        [sg.Text(current_rank)]
    ]

    progress_bar = [
        [sg.ProgressBar(max_value=1000, orientation='h', s=(10, 20), key="progressbar")]
    ]

    current = [
        [sg.Text("Current Rank:")]
    ]

    main_details = [
        [sg.Text("Name: " + name), sg.Text("Level: " + account_level), sg.Text(region)],
        [sg.Column(current, element_justification='c')]
    ]

    layout_l = [
        [sg.Text("Name: " + name), sg.Text("Level: " + account_level), sg.Text(region)],
        [sg.Text("Current Rank:")],
        [sg.Column([[rank]], justification='c')],
        [sg.Text(current_rank, justification='c')],
        [sg.Text(f"{ranking_in_tier} "), sg.Column(progress_bar), sg.Text("100")]
    ]

    layout_main = [
        [card],
        [sg.HorizontalSeparator()],
        [sg.Column(layout_l, element_justification='c', justification='c')],
        [sg.HorizontalSeparator()]
    ]

    window = sg.Window("MetaTrak", layout_main, icon='valorant.ico')

    progress_bar = window['progressbar']
    for i in range(1000):
        event, values = window.read(timeout=1000)
        if event == sg.WIN_CLOSED:
            break
        progress_bar.UpdateBar(ranking_in_tier * 10)

    window.close()

    return event, values


def all_data(name, id):
    global all_dicts, account_data, mmr_data, mmr_history, region_version, match_id, last_match_data
    all_dicts = allPlayerData(name, id)
    account_data = all_dicts[0]
    mmr_data = all_dicts[1]
    mmr_history = all_dicts[2]
    region_version = all_dicts[3]
    match_id = all_dicts[4]
    last_match_data = all_dicts[5]
    return all_dicts, account_data, mmr_data, mmr_history, region_version, match_id, last_match_data


def option_menu():
    sg.theme('DarkBlue')

    title = [
        [sg.Text("Please choose an option...")]
    ]

    buttons = [
        [sg.Button('Recent Match Overview')],
        [sg.Canvas()],
        [sg.Button('Leader Board')],
        [sg.Canvas()],
        [sg.Button('Specific Match Breakdown')]
    ]

    layout = [
        [sg.Column(title, element_justification='c', justification='c')],
        [sg.Column(buttons, justification='c')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico', size=(225, 175))
    event, values = window.read()
    window.close()

    return event, values


def recent_match_summary_option(all_dicts, playername):
    match_arr = []
    list = ['1', '2', '3']

    for i in range(1, 4):
        match_arr.append(all_dicts[0][4][i]['match_id'][0])
    # pp.pprint(match_arr)

    match1 = matchHistory(match_arr[0])
    meta1 = match1[0][1]
    players1 = match1[1]

    match2 = matchHistory(match_arr[1])
    meta2 = match2[0][1]
    players2 = match2[1]

    match3 = matchHistory(match_arr[2])
    meta3 = match3[0][1]
    players3 = match3[1]

    # print(playername)

    mmr1 = mmr_history[1]["mmr_change"][0]
    mmr2 = mmr_history[2]["mmr_change"][0]
    mmr3 = mmr_history[3]["mmr_change"][0]

    rr_array = [mmr1, mmr2, mmr3]
    main = format_rr(rr_array)

    for i in range(1, 11):
        name = players1[i]['name'][0]
        if name == playername:
            player_pos1 = i
            # print(i)

    for i in range(1, 11):
        name = players2[i]['name'][0]
        if name == playername:
            player_pos2 = i
            # print(i)

    for i in range(1, 11):
        name = players3[i]['name'][0]
        if name == playername:
            player_pos3 = i
            # print(i)

    character1 = players1[player_pos1]['character'][0]
    image1 = players1[player_pos1]['agent_kill_feed'][0]
    current_tier1 = players1[player_pos1]['current_tier'][0]
    kills1 = players1[player_pos1]['kills'][0]
    deaths1 = players1[player_pos1]['deaths'][0]
    assists1 = players1[player_pos1]['assists'][0]
    map1 = meta1['map'][0]
    mode1 = meta1['mode'][0]

    character2 = players2[player_pos2]['character'][0]
    image2 = players2[player_pos2]['agent_kill_feed'][0]
    current_tier2 = players2[player_pos2]['current_tier'][0]
    kills2 = players2[player_pos2]['kills'][0]
    deaths2 = players2[player_pos2]['deaths'][0]
    assists2 = players2[player_pos2]['assists'][0]
    map2 = meta2['map'][0]
    mode2 = meta2['mode'][0]

    character3 = players3[player_pos3]['character'][0]
    image3 = players3[player_pos3]['agent_kill_feed'][0]
    current_tier3 = players3[player_pos3]['current_tier'][0]
    kills3 = players3[player_pos3]['kills'][0]
    deaths3 = players3[player_pos3]['deaths'][0]
    assists3 = players3[player_pos3]['assists'][0]
    map3 = meta3['map'][0]
    mode3 = meta3['mode'][0]

    # print(character1, image2, map3)

    card1_bytes = requests.get(image1)
    card1_image = Image.open(io.BytesIO(card1_bytes.content))
    card1_png = io.BytesIO()
    card1_image.save(card1_png, format="PNG")
    card1_display = card1_png.getvalue()

    card2_bytes = requests.get(image2)
    card2_image = Image.open(io.BytesIO(card2_bytes.content))
    card2_png = io.BytesIO()
    card2_image.save(card2_png, format="PNG")
    card2_display = card2_png.getvalue()

    card3_bytes = requests.get(image3)
    card3_image = Image.open(io.BytesIO(card3_bytes.content))
    card3_png = io.BytesIO()
    card3_image.save(card3_png, format="PNG")
    card3_display = card3_png.getvalue()

    im1 = sg.Image(data=card1_display)
    im2 = sg.Image(data=card2_display)
    im3 = sg.Image(data=card3_display)

    layout = [
        [sg.Text("Recent Match Overview")],
        [im1, sg.Text(current_tier1), sg.Text(mmr1), sg.Text(map1), sg.Text(mode1)],
        [sg.Text("Kills: " + str(kills1)), sg.Text("Deaths: " + str(deaths1)), sg.Text("Assists: " + str(assists1))],
        [im2, sg.Text(current_tier2), sg.Text(mmr2), sg.Text(map2), sg.Text(mode2)],
        [sg.Text("Kills: " + str(kills2)), sg.Text("Deaths: " + str(deaths2)), sg.Text("Assists: " + str(assists2))],
        [im3, sg.Text(current_tier3), sg.Text(mmr3), sg.Text(map3), sg.Text(mode3)],
        [sg.Text("Kills: " + str(kills3)), sg.Text("Deaths: " + str(deaths3)), sg.Text("Assists: " + str(assists3))]
    ]

    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()
    return event, values


def leaderboard_option():
    leader_dict = getLeaderboard("eu", 1000)
    leaderboard_display(leader_dict)


types_of_data = ['name', 'tag', 'team', 'level', 'character', 'c_casts', 'e_cast', 'q_casts', 'agent_kill_feed',
                 'score', 'kills', 'deaths', 'assists', 'bodyshots', 'headshots', 'legshots',
                 'damage_made', 'damage_received', 'spent_avg', 'spent_overall']


def define_players(player: int, red_players: dict, blue_players: dict, players):
    if players[player]['team'][0] == "Red":
        name = f"red{(len(red_players) // 20) + 1}"
        for item in types_of_data:
            red_players[f"{name}_{item}"] = players[player][item][0]
    else:
        name = f"blue{(len(blue_players) // 20) + 1}"
        for item in types_of_data:
            blue_players[f"{name}_{item}"] = players[player][item][0]
    return red_players, blue_players


def match_breakdown_option(all_dicts):
    sg.theme('DarkBlue')

    match_id = all_dicts[0][4][1]['match_id'][0]
    match = matchHistory(match_id)
    metadata = match[0][1]
    players = match[1]
    # pp.pprint(metadata)
    # print("------------------------------------------------------------")
    # pp.pprint(players)

    red = []
    blue = []

    for i in range(1, 11):
        player_team = players[i]['team'][0]
        if player_team == "Red":
            red.append(i)
        elif player_team == "Blue":
            blue.append(i)

    print(red)
    print("-----------")
    print(blue)
    print("-----------")

    # asdasd
    red_players = {}
    blue_players = {}
    for player in range(1, 11):
        red_players, blue_players = define_players(player, red_players, blue_players, players)
    pp.pprint(red_players)
    pp.pprint(blue_players)

    red1_tab = [
        [sg.Text("Level: " + str(red_players['red1_level']))],
        [sg.Text("Character: " + red_players['red1_character'])],
        [sg.Text("C Casts: " + str(red_players['red1_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red1_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red1_q_casts']))],
        [sg.Text("ACS: " + str(red_players['red1_score']))],
        [sg.Text("Kills: " + str(red_players['red1_kills']))],
        [sg.Text("Deaths: " + str(red_players['red1_deaths']))],
        [sg.Text("Assist: " + str(red_players['red1_assists']))],
        [sg.Text("H/S %: " + str(((red_players['red1_headshots']) / (red_players['red1_headshots']
                                                                 + red_players['red1_bodyshots'] + red_players[
                                                                     'red1_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(red_players['red1_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red1_damage_received']))]
    ]

    red2_tab = [
        [sg.Text("Level: " + str(red_players['red2_level']))],
        [sg.Text("Character: " + str(red_players['red2_character']))],
        [sg.Text("C Casts: " + str(red_players['red2_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red2_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red2_q_casts']))],
        [sg.Text("ACS: " + str(red_players['red2_score']))],
        [sg.Text("Kills: " + str(red_players['red2_kills']))],
        [sg.Text("Deaths: " + str(red_players['red2_deaths']))],
        [sg.Text("Assist: " + str(red_players['red2_assists']))],
        [sg.Text("H/S %: " + str(((red_players['red2_headshots']) / (red_players['red2_headshots']
                                                                 + red_players['red2_bodyshots'] + red_players[
                                                                     'red2_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(red_players['red2_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red2_damage_received']))]
    ]

    red3_tab = [
        [sg.Text("Level: " + str(red_players['red3_level']))],
        [sg.Text("Character: " + str(red_players['red3_character']))],
        [sg.Text("C Casts: " + str(red_players['red3_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red3_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red3_q_casts']))],
        [sg.Text("ACS: " + str(red_players['red3_score']))],
        [sg.Text("Kills: " + str(red_players['red3_kills']))],
        [sg.Text("Deaths: " + str(red_players['red3_deaths']))],
        [sg.Text("Assist: " + str(red_players['red3_assists']))],
        [sg.Text("H/S %: " + str(((red_players['red3_headshots']) / (red_players['red3_headshots']
                                                                 + red_players['red3_bodyshots'] + red_players[
                                                                     'red3_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(red_players['red3_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red3_damage_received']))]
    ]

    red4_tab = [
        [sg.Text("Level: " + str(red_players['red4_level']))],
        [sg.Text("Character: " + str(red_players['red4_character']))],
        [sg.Text("C Casts: " + str(red_players['red4_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red4_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red4_q_casts']))],
        [sg.Text("ACS: " + str(red_players['red4_score']))],
        [sg.Text("Kills: " + str(red_players['red4_kills']))],
        [sg.Text("Deaths: " + str(red_players['red4_deaths']))],
        [sg.Text("Assist: " + str(red_players['red4_assists']))],
        [sg.Text("H/S %: " + str(((red_players['red4_headshots']) / (red_players['red4_headshots']
                                                                 + red_players['red4_bodyshots'] + red_players[
                                                                     'red4_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(red_players['red4_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red4_damage_received']))]
    ]

    red5_tab = [
        [sg.Text("Level: " + str(red_players['red5_level']))],
        [sg.Text("Character: " + str(red_players['red5_character']))],
        [sg.Text("C Casts: " + str(red_players['red5_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red5_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red5_q_casts']))],
        [sg.Text("ACS: " + str(red_players['red5_score']))],
        [sg.Text("Kills: " + str(red_players['red5_kills']))],
        [sg.Text("Deaths: " + str(red_players['red5_deaths']))],
        [sg.Text("Assist: " + str(red_players['red5_assists']))],
        [sg.Text("H/S %: " + str(((red_players['red5_headshots']) / (red_players['red5_headshots']
                                                                 + red_players['red5_bodyshots'] + red_players[
                                                                     'red5_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(red_players['red5_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red5_damage_received']))]
    ]

    blue1_tab = [
        [sg.Text("Level: " + str(blue_players['blue1_level']))],
        [sg.Text("Character: " + str(blue_players['blue1_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue1_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue1_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue1_q_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue1_score']))],
        [sg.Text("Kills: " + str(blue_players['blue1_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue1_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue1_assists']))],
        [sg.Text("H/S %: " + str(((blue_players['blue1_headshots']) / (blue_players['blue1_headshots']
                                                                   + blue_players['blue1_bodyshots'] + blue_players[
                                                                       'blue1_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue1_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue1_damage_received']))]
    ]

    blue2_tab = [
        [sg.Text("Level: " + str(blue_players['blue2_level']))],
        [sg.Text("Character: " + str(blue_players['blue2_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue2_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue2_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue2_q_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue2_score']))],
        [sg.Text("Kills: " + str(blue_players['blue2_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue2_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue2_assists']))],
        [sg.Text("H/S %: " + str(((blue_players['blue2_headshots']) / (blue_players['blue2_headshots']
                                                                   + blue_players['blue2_bodyshots'] + blue_players[
                                                                       'blue2_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue2_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue2_damage_received']))]
    ]

    blue3_tab = [
        [sg.Text("Level: " + str(blue_players['blue3_level']))],
        [sg.Text("Character: " + str(blue_players['blue3_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue3_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue3_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue3_q_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue3_score']))],
        [sg.Text("Kills: " + str(blue_players['blue3_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue3_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue3_assists']))],
        [sg.Text("H/S %: " + str(((blue_players['blue3_headshots']) / (blue_players['blue3_headshots']
                                                                   + blue_players['blue3_bodyshots'] + blue_players[
                                                                       'blue3_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue3_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue3_damage_received']))]
    ]

    blue4_tab = [
        [sg.Text("Level: " + str(blue_players['blue4_level']))],
        [sg.Text("Character: " + str(blue_players['blue4_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue4_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue4_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue4_q_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue4_score']))],
        [sg.Text("Kills: " + str(blue_players['blue4_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue4_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue4_assists']))],
        [sg.Text("H/S %: " + str(((blue_players['blue4_headshots']) / (blue_players['blue4_headshots']
                                                                   + blue_players['blue4_bodyshots'] + blue_players[
                                                                       'blue4_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue4_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue4_damage_received']))]
    ]

    blue5_tab = [
        [sg.Text("Level: " + str(blue_players['blue5_level']))],
        [sg.Text("Character: " + str(blue_players['blue5_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue5_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue5_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue5_q_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue5_score']))],
        [sg.Text("Kills: " + str(blue_players['blue5_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue5_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue5_assists']))],
        [sg.Text("H/S %: " + str(((blue_players['blue5_headshots']) / (blue_players['blue5_headshots']
                                                                   + blue_players['blue5_bodyshots'] + blue_players[
                                                                       'blue5_legshots'])) * 100))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue5_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue5_damage_received']))]
    ]

    l_layout = [
        [sg.TabGroup([[sg.Tab((red_players['red1_name'] + " " + red_players['red1_tag']), red1_tab),
                       sg.Tab((red_players['red2_name'] + " " + red_players['red2_tag']), red2_tab),
                       sg.Tab((red_players['red3_name'] + " " + red_players['red3_tag']), red3_tab),
                       sg.Tab((red_players['red4_name'] + " " + red_players['red4_tag']), red4_tab),
                       sg.Tab((red_players['red5_name'] + " " + red_players['red5_tag']), red5_tab)


                       ]])]

    ]

    layout = [
        [sg.Column(l_layout, justification="l")]
    ]

    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()
    return event, values


def choice(option_choice, all_dicts, playername):
    if option_choice == "Recent Match Overview":
        recent_match_summary_option(all_dicts, playername)
    elif option_choice == "Leader Board":
        leaderboard_option()
    elif option_choice == "Specific Match Breakdown":
        match_breakdown_option(all_dicts)


def leaderboard_display(dict):
    sg.theme('DarkBlue')
    page = 1

    def pagedict(pagenum, dictionary):
        pagestart = (pagenum * 10) - 9
        pageend = (pagenum * 10)
        sub_dict = {
            0: {
                "name": ["test"],
                "tag": ["123"],
                "wins": ["---"]
            }
        }
        for i in range(pagestart, pageend + 1):
            sub_dict[i] = dictionary[i]

        return sub_dict

    layout = [[sg.Slider(range=(1, 100), orientation='h', change_submits=True, key='slider'),
               sg.Text(str(page), key='text')],
              [sg.Text("Move", key='rank1'), sg.Text("Slider", key='name1'), sg.Text("To", key='tag1'),
               sg.Text("Start", key='wins1')],

              [sg.Text("Move", key='rank2'), sg.Text("Slider", key='name2'), sg.Text("To", key='tag2'),
               sg.Text("Start", key='wins2')],

              [sg.Text("Move", key='rank3'), sg.Text("Slider", key='name3'), sg.Text("To", key='tag3'),
               sg.Text("Start", key='wins3')],

              [sg.Text("Move", key='rank4'), sg.Text("Slider", key='name4'), sg.Text("To", key='tag4'),
               sg.Text("Start", key='wins4')],

              [sg.Text("Move", key='rank5'), sg.Text("Slider", key='name5'), sg.Text("To", key='tag5'),
               sg.Text("Start", key='wins5')],

              [sg.Text("Move", key='rank6'), sg.Text("Slider", key='name6'), sg.Text("To", key='tag6'),
               sg.Text("Start", key='wins6')],

              [sg.Text("Move", key='rank7'), sg.Text("Slider", key='name7'), sg.Text("To", key='tag7'),
               sg.Text("Start", key='wins7')],

              [sg.Text("Move", key='rank8'), sg.Text("Slider", key='name8'), sg.Text("To", key='tag8'),
               sg.Text("Start", key='wins8')],

              [sg.Text("Move", key='rank9'), sg.Text("Slider", key='name9'), sg.Text("To", key='tag9'),
               sg.Text("Start", key='wins9')],

              [sg.Text("Move", key='rank10'), sg.Text("Slider", key='name10'), sg.Text("To", key='tag10'),
               sg.Text("Start", key='wins10')],

              ]

    pg = page
    window = sg.Window("MetaTrak", layout, icon='valorant.ico', grab_anywhere=False, size=(300, 300))
    # Event Loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        pg_slider = int(values['slider'])
        pg = pg_slider
        window['slider'].update(56)
        window['slider'].update(1)
        if pg != page:
            players = pagedict(pg, dict)
            pagestart = (pg * 10) - 9
            pageend = (pg * 10)

            page = pg
            window['slider'].update(pg)
            window['text'].update(pg)

            for i in range(0, 10):
                window[f'rank{i + 1}'].update(pagestart + i)
                window[f'name{i + 1}'].update(players[pagestart + i]["Name"][0])
                window[f'tag{i + 1}'].update(players[pagestart + i]["Tag"][0])
                window[f'wins{i + 1}'].update(players[pagestart + i]["Wins"][0])
                if players[pagestart + i]["Name"][0] == "" or players[pagestart + i]["Tag"][0] == "":
                    window[f'name{i + 1}'].update("Anon")
                    window[f'tag{i + 1}'].update("Anon")


if __name__ == '__main__':
    # main_login()

    details = api_login()
    all_dicts = all_data(details[0], details[1])
    # pp.pprint(all_dicts[0][0])

    # loading()
    # recent_match_summary_option()

    popup("Close the main menu when you would like to select another option.")
    main_menu()
    option_choice = option_menu()

    # print(option_choice[0])
    choice(option_choice[0], all_dicts, details[0])

    # leader_data = leaderboard_inp_window()
    # print(leader_data)
    # getLeaderboard("eu", int(leader_data[1][0]))
