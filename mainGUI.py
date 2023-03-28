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


def match_breakdown_option(all_dicts):
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

    red1_name = players[red[0]]['name'][0]
    red1_tag = players[red[0]]['tag'][0]
    red1_level = players[red[0]]['level'][0]
    red1_character = players[red[0]]['character'][0]
    red1_c_casts = players[red[0]]['c_casts'][0]
    red1_e_casts = players[red[0]]['e_cast'][0]
    red1_q_casts = players[red[0]]['q_casts'][0]
    red1_agent_image = players[red[0]]['agent_kill_feed'][0]
    red1_score = players[red[0]]['score'][0]
    red1_kills = players[red[0]]['kills'][0]
    red1_deaths = players[red[0]]['deaths'][0]
    red1_assists = players[red[0]]['assists'][0]
    red1_bodyshots = players[red[0]]['bodyshots'][0]
    red1_headshots = players[red[0]]['headshots'][0]
    red1_legshots = players[red[0]]['legshots'][0]
    red1_damage_made = players[red[0]]['damage_made'][0]
    red1_damage_recieved = players[red[0]]['damage_received'][0]
    red1_spent_avg = players[red[0]]['spent_avg'][0]
    red1_spent_overall = players[red[0]]['spent_overall'][0]

    red2_name = players[red[0]]['name'][0]
    red2_tag = players[red[0]]['tag'][0]
    red2_level = players[red[0]]['level'][0]
    red2_character = players[red[0]]['character'][0]
    red2_c_casts = players[red[0]]['c_casts'][0]
    red2_e_casts = players[red[0]]['e_cast'][0]
    red2_q_casts = players[red[0]]['q_casts'][0]
    red2_agent_image = players[red[0]]['agent_kill_feed'][0]
    red2_score = players[red[0]]['score'][0]
    red2_kills = players[red[0]]['kills'][0]
    red2_deaths = players[red[0]]['deaths'][0]
    red2_assists = players[red[0]]['assists'][0]
    red2_bodyshots = players[red[0]]['bodyshots'][0]
    red2_headshots = players[red[0]]['headshots'][0]
    red2_legshots = players[red[0]]['legshots'][0]
    red2_damage_made = players[red[0]]['damage_made'][0]
    red2_damage_recieved = players[red[0]]['damage_received'][0]
    red2_spent_avg = players[red[0]]['spent_avg'][0]
    red2_spent_overall = players[red[0]]['spent_overall'][0]

    red3_name = players[red[0]]['name'][0]
    red3_tag = players[red[0]]['tag'][0]
    red3_level = players[red[0]]['level'][0]
    red3_character = players[red[0]]['character'][0]
    red3_c_casts = players[red[0]]['c_casts'][0]
    red3_e_casts = players[red[0]]['e_cast'][0]
    red3_q_casts = players[red[0]]['q_casts'][0]
    red3_agent_image = players[red[0]]['agent_kill_feed'][0]
    red3_score = players[red[0]]['score'][0]
    red3_kills = players[red[0]]['kills'][0]
    red3_deaths = players[red[0]]['deaths'][0]
    red3_assists = players[red[0]]['assists'][0]
    red3_bodyshots = players[red[0]]['bodyshots'][0]
    red3_headshots = players[red[0]]['headshots'][0]
    red3_legshots = players[red[0]]['legshots'][0]
    red3_damage_made = players[red[0]]['damage_made'][0]
    red3_damage_recieved = players[red[0]]['damage_received'][0]
    red3_spent_avg = players[red[0]]['spent_avg'][0]
    red3_spent_overall = players[red[0]]['spent_overall'][0]

    red4_name = players[red[0]]['name'][0]
    red4_tag = players[red[0]]['tag'][0]
    red4_level = players[red[0]]['level'][0]
    red4_character = players[red[0]]['character'][0]
    red4_c_casts = players[red[0]]['c_casts'][0]
    red4_e_casts = players[red[0]]['e_cast'][0]
    red4_q_casts = players[red[0]]['q_casts'][0]
    red4_agent_image = players[red[0]]['agent_kill_feed'][0]
    red4_score = players[red[0]]['score'][0]
    red4_kills = players[red[0]]['kills'][0]
    red4_deaths = players[red[0]]['deaths'][0]
    red4_assists = players[red[0]]['assists'][0]
    red4_bodyshots = players[red[0]]['bodyshots'][0]
    red4_headshots = players[red[0]]['headshots'][0]
    red4_legshots = players[red[0]]['legshots'][0]
    red4_damage_made = players[red[0]]['damage_made'][0]
    red4_damage_recieved = players[red[0]]['damage_received'][0]
    red4_spent_avg = players[red[0]]['spent_avg'][0]
    red4_spent_overall = players[red[0]]['spent_overall'][0]

    red5_name = players[red[0]]['name'][0]
    red5_tag = players[red[0]]['tag'][0]
    red5_level = players[red[0]]['level'][0]
    red5_character = players[red[0]]['character'][0]
    red5_c_casts = players[red[0]]['c_casts'][0]
    red5_e_casts = players[red[0]]['e_cast'][0]
    red5_q_casts = players[red[0]]['q_casts'][0]
    red5_agent_image = players[red[0]]['agent_kill_feed'][0]
    red5_score = players[red[0]]['score'][0]
    red5_kills = players[red[0]]['kills'][0]
    red5_deaths = players[red[0]]['deaths'][0]
    red5_assists = players[red[0]]['assists'][0]
    red5_bodyshots = players[red[0]]['bodyshots'][0]
    red5_headshots = players[red[0]]['headshots'][0]
    red5_legshots = players[red[0]]['legshots'][0]
    red5_damage_made = players[red[0]]['damage_made'][0]
    red5_damage_recieved = players[red[0]]['damage_received'][0]
    red5_spent_avg = players[red[0]]['spent_avg'][0]
    red5_spent_overall = players[red[0]]['spent_overall'][0]

    blue1_name = players[blue[0]]['name'][0]
    blue1_tag = players[blue[0]]['tag'][0]
    blue1_level = players[blue[0]]['level'][0]
    blue1_character = players[blue[0]]['character'][0]
    blue1_c_casts = players[blue[0]]['c_casts'][0]
    blue1_e_casts = players[blue[0]]['e_cast'][0]
    blue1_q_casts = players[blue[0]]['q_casts'][0]
    blue1_agent_image = players[blue[0]]['agent_kill_feed'][0]
    blue1_score = players[blue[0]]['score'][0]
    blue1_kills = players[blue[0]]['kills'][0]
    blue1_deaths = players[blue[0]]['deaths'][0]
    blue1_assists = players[blue[0]]['assists'][0]
    blue1_bodyshots = players[blue[0]]['bodyshots'][0]
    blue1_headshots = players[blue[0]]['headshots'][0]
    blue1_legshots = players[blue[0]]['legshots'][0]
    blue1_damage_made = players[blue[0]]['damage_made'][0]
    blue1_damage_recieved = players[blue[0]]['damage_received'][0]
    blue1_spent_avg = players[blue[0]]['spent_avg'][0]
    blue1_spent_overall = players[blue[0]]['spent_overall'][0]

    blue2_name = players[blue[0]]['name'][0]
    blue2_tag = players[blue[0]]['tag'][0]
    blue2_level = players[blue[0]]['level'][0]
    blue2_character = players[blue[0]]['character'][0]
    blue2_c_casts = players[blue[0]]['c_casts'][0]
    blue2_e_casts = players[blue[0]]['e_cast'][0]
    blue2_q_casts = players[blue[0]]['q_casts'][0]
    blue2_agent_image = players[blue[0]]['agent_kill_feed'][0]
    blue2_score = players[blue[0]]['score'][0]
    blue2_kills = players[blue[0]]['kills'][0]
    blue2_deaths = players[blue[0]]['deaths'][0]
    blue2_assists = players[blue[0]]['assists'][0]
    blue2_bodyshots = players[blue[0]]['bodyshots'][0]
    blue2_headshots = players[blue[0]]['headshots'][0]
    blue2_legshots = players[blue[0]]['legshots'][0]
    blue2_damage_made = players[blue[0]]['damage_made'][0]
    blue2_damage_recieved = players[blue[0]]['damage_received'][0]
    blue2_spent_avg = players[blue[0]]['spent_avg'][0]
    blue2_spent_overall = players[blue[0]]['spent_overall'][0]

    blue3_name = players[blue[0]]['name'][0]
    blue3_tag = players[blue[0]]['tag'][0]
    blue3_level = players[blue[0]]['level'][0]
    blue3_character = players[blue[0]]['character'][0]
    blue3_c_casts = players[blue[0]]['c_casts'][0]
    blue3_e_casts = players[blue[0]]['e_cast'][0]
    blue3_q_casts = players[blue[0]]['q_casts'][0]
    blue3_agent_image = players[blue[0]]['agent_kill_feed'][0]
    blue3_score = players[blue[0]]['score'][0]
    blue3_kills = players[blue[0]]['kills'][0]
    blue3_deaths = players[blue[0]]['deaths'][0]
    blue3_assists = players[blue[0]]['assists'][0]
    blue3_bodyshots = players[blue[0]]['bodyshots'][0]
    blue3_headshots = players[blue[0]]['headshots'][0]
    blue3_legshots = players[blue[0]]['legshots'][0]
    blue3_damage_made = players[blue[0]]['damage_made'][0]
    blue3_damage_recieved = players[blue[0]]['damage_received'][0]
    blue3_spent_avg = players[blue[0]]['spent_avg'][0]
    blue3_spent_overall = players[blue[0]]['spent_overall'][0]

    blue4_name = players[blue[0]]['name'][0]
    blue4_tag = players[blue[0]]['tag'][0]
    blue4_level = players[blue[0]]['level'][0]
    blue4_character = players[blue[0]]['character'][0]
    blue4_c_casts = players[blue[0]]['c_casts'][0]
    blue4_e_casts = players[blue[0]]['e_cast'][0]
    blue4_q_casts = players[blue[0]]['q_casts'][0]
    blue4_agent_image = players[blue[0]]['agent_kill_feed'][0]
    blue4_score = players[blue[0]]['score'][0]
    blue4_kills = players[blue[0]]['kills'][0]
    blue4_deaths = players[blue[0]]['deaths'][0]
    blue4_assists = players[blue[0]]['assists'][0]
    blue4_bodyshots = players[blue[0]]['bodyshots'][0]
    blue4_headshots = players[blue[0]]['headshots'][0]
    blue4_legshots = players[blue[0]]['legshots'][0]
    blue4_damage_made = players[blue[0]]['damage_made'][0]
    blue4_damage_recieved = players[blue[0]]['damage_received'][0]
    blue4_spent_avg = players[blue[0]]['spent_avg'][0]
    blue4_spent_overall = players[blue[0]]['spent_overall'][0]

    blue5_name = players[blue[0]]['name'][0]
    blue5_tag = players[blue[0]]['tag'][0]
    blue5_level = players[blue[0]]['level'][0]
    blue5_character = players[blue[0]]['character'][0]
    blue5_c_casts = players[blue[0]]['c_casts'][0]
    blue5_e_casts = players[blue[0]]['e_cast'][0]
    blue5_q_casts = players[blue[0]]['q_casts'][0]
    blue5_agent_image = players[blue[0]]['agent_kill_feed'][0]
    blue5_score = players[blue[0]]['score'][0]
    blue5_kills = players[blue[0]]['kills'][0]
    blue5_deaths = players[blue[0]]['deaths'][0]
    blue5_assists = players[blue[0]]['assists'][0]
    blue5_bodyshots = players[blue[0]]['bodyshots'][0]
    blue5_headshots = players[blue[0]]['headshots'][0]
    blue5_legshots = players[blue[0]]['legshots'][0]
    blue5_damage_made = players[blue[0]]['damage_made'][0]
    blue5_damage_recieved = players[blue[0]]['damage_received'][0]
    blue5_spent_avg = players[blue[0]]['spent_avg'][0]
    blue5_spent_overall = players[blue[0]]['spent_overall'][0]




    tab1_layout = [

    ]

    layout = [
        [sg.Text("sadf")]
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
