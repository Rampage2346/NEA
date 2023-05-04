# importing the GUI
import PySimpleGUI as sg
# importing to display dictionaries better
import pprint
import requests
# using pillow library to request and display images
from PIL import Image
import io
# importing algorithms from other python files in the program
from login import checkPass, addUser
from MainAPICall import allPlayerData, format_rr, getLeaderboard, matchHistory

pp = pprint.PrettyPrinter(sort_dicts=False)


def popup(message):
    """This function is used to create one time windows that display the text given in the parameter message"""
    # defines the theme of the window
    sg.theme('DarkBlue')
    # defines column
    column_to_be_centered = [
        [sg.Text(message)],
        [sg.Push(), sg.Button('OK')]
    ]

    # uses column and gives a central justification attribute. Also uses VPush and Push to centre text.
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]
    # defines the window and gives it a title and an icon
    sg.Window('MetaTrak', layout, modal=True, icon='valorant.ico').read(close=True)


def checkLength(new_user_creds):
    """This function is used to check if the new users username and password meet the length requirement"""
    len_user = False
    len_pass = False

    if 4 < len(new_user_creds[1][0]) < 9:
        len_user = True
    if 4 < len(new_user_creds[1][1]) < 9:
        len_pass = True

    while len_user == False or len_pass == False:
        popup("Please make sure that both your username and password are of the correct length")
        new_user_creds = new_user_window()
        if 4 < len(new_user_creds[1][0]) < 9:
            len_user = True
        if 4 < len(new_user_creds[1][1]) < 9:
            len_pass = True

    return len_user, len_pass


def login_or_adduser():
    """This function gives the user the option to either log in with an existing account or create a new one.
    It returns the event that the user selected"""
    # defines the theme of the window
    sg.theme('DarkBlue')
    # defines layout using a series of text boxes and buttons
    layout = [
        [sg.Canvas()],
        [sg.Canvas(), sg.Text("Please Choose an Option:"), sg.Canvas()],
        [sg.Canvas()],
        [sg.Canvas(), sg.Button("I already have an account"), sg.Button("I am a new user"), sg.Canvas()]
    ]
    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event from the window
    event = window.read()
    # automatically closes the window once an event has been triggered
    window.close()

    return event


def login_window():
    """This function asks the user to enter their username and password. Once the submit event is triggered the values 
    are read and return as event and values"""
    # defines the theme of the window
    sg.theme('DarkBlue')
    # defines layout using a series of text boxes, userinput text and buttons
    layout = [
        [sg.Text('Enter Your Username')],
        [sg.InputText()],
        [sg.Text('Enter Your Password')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event and the values provided from the window
    event, values = window.read()
    # automatically closes the window once an event has been triggered
    window.close()

    return event, values


def new_user_window():
    """This function asks the user to create new login details then returns them"""
    # defines the theme of the window
    sg.theme('DarkBlue')
    # defines layout using a series of text boxes, userinput text and buttons
    layout = [
        [sg.Text('Enter Your New Username (between 4 and 9 characters):')],
        [sg.InputText()],
        [sg.Text('Enter Your New Password (between 4 and 9 characters):')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event and the values provided from the window
    event, values = window.read()
    # automatically closes the window once an event has been triggered
    window.close()

    return event, values


def api_login_window():
    """This function prompts the user to enter their RIOT name and tag then returns the values provided"""
    # defines the theme of the window
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Enter Your Riot ID:')],
        [sg.InputText()],
        [sg.Text('Enter Your Tagline:')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event and the values provided from the window
    event, values = window.read()
    # automatically closes the window once an event has been triggered
    window.close()

    return event, values


def main_login():
    """This subroutine explains the basics of the program and then calls the login_or_adduser() function and uses
    the result to either call the login window or the create existing user window"""
    popup("Welcome To MetaTrak, a python application responsible for your imminent improvement at Valorant! \nOn the "
          "next screen you will need to login or create a new account.")
    # calls function and saves the users choice
    login_choice = login_or_adduser()

    # if the user has an account a window is called and the user enters a username and password until it is correct
    if login_choice[0] == "I already have an account":
        check = False
        login_inp_array = login_window()
        if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        check = checkPass(login_inp_array[1][0], login_inp_array[1][1])
        while check is False:
            popup("Incorrect Username or Password!\nPlease try again.")
            login_inp_array = login_window()
            if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
                exit()
            check = checkPass(login_inp_array[1][0], login_inp_array[1][1])

    # if the user does not have an account a window is called where they can enter their new login, makes
    # sure that the username and password are within the given length boundaries
    elif login_choice[0] == "I am a new user":
        new_user_inp_array = new_user_window()
        checkLength(new_user_inp_array)

        if new_user_inp_array[0] == 'Cancel' or new_user_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        addUser(new_user_inp_array[1][0], new_user_inp_array[1][1])


def api_login():
    """This function describes the way in which the user should enter their account details.
    It then calls an input window and returns the users details"""
    popup("You have now logged in or created your new account. Now you will need to provide the Valorant account \n"
          "that you would like to fetch the stats for. This means your IGN and your tagline, the string after the #.\n")
    api_inp_array = api_login_window()
    return api_inp_array[1][0], api_inp_array[1][1]


def main_menu():
    """This function is the main window that is opened after logging in with you RIOT account details"""
    # defines the theme of the window
    sg.theme('DarkBlue')

    # this block of code is repeated multiple times throughout this program
    # this uses the requests module to fetch the image from the URL and then using the io library
    # it formats it into something that PySimpleGUI can display
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

    # this ProgressBar element is used as a static bar to display the players ranked rating out of 100
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

    layout = [
        [sg.Text("Name: " + name), sg.Text("Level: " + account_level), sg.Text(region)],
        [sg.Text("Current Rank:")],
        [sg.Column([[rank]], justification='c')],
        [sg.Text(current_rank, justification='c')],
        [sg.Text(f"{ranking_in_tier} "), sg.Column(progress_bar), sg.Text("100")]
    ]
    # defines layout with horizontal separators to divide the window
    layout_main = [
        [card],
        [sg.HorizontalSeparator()],
        [sg.Column(layout, element_justification='c', justification='c')],
        [sg.HorizontalSeparator()]
    ]

    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout_main, icon='valorant.ico')

    # uses the key of the progress bar and a for loop to increase the value up to the players current rank
    progress_bar = window['progressbar']
    for i in range(1000):
        event, values = window.read(timeout=1000)
        if event == sg.WIN_CLOSED:
            break
        progress_bar.UpdateBar(ranking_in_tier * 10)

    window.close()

    return event, values


def all_data(name, id):
    """This function is reponsible for calling all functions that request data from the API with
    RIOT name and tag as parameters"""
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
    """This function creates a window that asks the user which of the 3 main function they would like to run.
    Returns the event"""
    # defines the theme of the window
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
    # defines the layout using columns to centre the title and buttons
    layout = [
        [sg.Column(title, element_justification='c', justification='c')],
        [sg.Column(buttons, justification='c')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico', size=(225, 175))
    # this reads the event and the values provided from the window
    event, values = window.read()
    # automatically closes the window once an event has been triggered
    window.close()

    return event, values


def recent_match_summary_option(all_dicts, playername):
    """This function fetches the 3 previous matches then filters through each match finding the players data
    such as win or loss and the map they played on as well an image of the agent they were playing"""
    match_arr = []

    # uses iteration to add the 3 previous match IDs to an array
    for i in range(1, 4):
        match_arr.append(all_dicts[0][4][i]['match_id'][0])

    # requests the match history of each ID and splits them into the match metadata and the individual player stats
    match1 = matchHistory(match_arr[0])
    meta1 = match1[0][1]
    players1 = match1[1]

    match2 = matchHistory(match_arr[1])
    meta2 = match2[0][1]
    players2 = match2[1]

    match3 = matchHistory(match_arr[2])
    meta3 = match3[0][1]
    players3 = match3[1]

    # gets the 3 most recent mmr changes to determine a loss or gain of x rr
    mmr1 = mmr_history[1]["mmr_change"][0]
    mmr2 = mmr_history[2]["mmr_change"][0]
    mmr3 = mmr_history[3]["mmr_change"][0]

    # puts the mmr values into an array and calls the format_rr() function to reformat the array
    rr_array = [mmr1, mmr2, mmr3]
    main = format_rr(rr_array)

    # these for loops iterate through the player dictionary in each match to find the number key
    # of the player that is logged in
    for i in range(1, 11):
        name = players1[i]['name'][0]
        if name == playername:
            player_pos1 = i

    for i in range(1, 11):
        name = players2[i]['name'][0]
        if name == playername:
            player_pos2 = i

    for i in range(1, 11):
        name = players3[i]['name'][0]
        if name == playername:
            player_pos3 = i

    # creates all variables for the players data in each map by using the correct player number key
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

    # this uses the requests module to fetch the image from the URL and then using the io library
    # it formats it into something that PySimpleGUI can display
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

    # defines the layout using a series of images and text
    layout = [
        [sg.Text("Recent Match Overview")],
        [im1, sg.Text(current_tier1), sg.Text(main[0]), sg.Text(map1), sg.Text(mode1)],
        [sg.Text("Kills: " + str(kills1)), sg.Text("Deaths: " + str(deaths1)), sg.Text("Assists: " + str(assists1))],
        [im2, sg.Text(current_tier2), sg.Text(main[1]), sg.Text(map2), sg.Text(mode2)],
        [sg.Text("Kills: " + str(kills2)), sg.Text("Deaths: " + str(deaths2)), sg.Text("Assists: " + str(assists2))],
        [im3, sg.Text(current_tier3), sg.Text(main[2]), sg.Text(map3), sg.Text(mode3)],
        [sg.Text("Kills: " + str(kills3)), sg.Text("Deaths: " + str(deaths3)), sg.Text("Assists: " + str(assists3))]
    ]

    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event and the values provided from the window
    event, values = window.read()
    window.close()
    return event, values


def leaderboard_option():
    """This function fetches the top 999 players and passes them to the leaderboard display window"""
    leader_dict = getLeaderboard("eu", 1000)
    leaderboard_display(leader_dict)


# this array contain all types of data the player can request
# and is used to create team and player specific dictionaries
types_of_data = ['name', 'tag', 'team', 'level', 'character', 'c_casts', 'e_cast', 'q_casts', 'x_casts',
                 'agent_kill_feed',
                 'score', 'kills', 'deaths', 'assists', 'bodyshots', 'headshots', 'legshots',
                 'damage_made', 'damage_received', 'spent_avg', 'spent_overall']


def define_players(player: int, red_players: dict, blue_players: dict, players):
    """This function checks to see if the player belong in the red or blue team
    and then generates, using f-strings and the array above, a dictionary
    based on player number, team and the different types of data. Takes the red and blue players dictionaries
     as parameters and return the 2 dictionaries containing all data"""
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
    """This function fetches the most recent match ID, queries the data and sends it to define_players() to
    create a player and team specific dictionary. It then creates multiple Tab elements to display
     the player data in a more compact way"""
    # defines the theme of the window
    sg.theme('DarkBlue')

    # fetches most recent match ID and fetches data using said ID
    match_id = all_dicts[0][4][1]['match_id'][0]
    match = matchHistory(match_id)

    # separates data
    metadata = match[0][1]
    players = match[1]

    # initialises dictionaries for both the red and blue players
    red_players = {}
    blue_players = {}
    # calls the define_players() function to create team and player specific dictionaries
    for player in range(1, 11):
        red_players, blue_players = define_players(player, red_players, blue_players, players)

    # defines all tabs for each team using the dictionaries created by the function above
    red1_tab = [
        [sg.Text("Level: " + str(red_players['red1_level']))],
        [sg.Text("Agent: " + red_players['red1_character'])],
        [sg.Text("C Casts: " + str(red_players['red1_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red1_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red1_q_casts']))],
        [sg.Text("X Casts: " + str(red_players['red1_x_casts']))],
        [sg.Text("ACS: " + str(red_players['red1_score']))],
        [sg.Text("Kills: " + str(red_players['red1_kills']))],
        [sg.Text("Deaths: " + str(red_players['red1_deaths']))],
        [sg.Text("Assist: " + str(red_players['red1_assists']))],
        [sg.Text("H/S %: " + str(round(((red_players['red1_headshots']) / (red_players['red1_headshots']
                                                                           + red_players['red1_bodyshots'] +
                                                                           red_players[
                                                                               'red1_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(red_players['red1_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red1_damage_received']))]
    ]

    red2_tab = [
        [sg.Text("Level: " + str(red_players['red2_level']))],
        [sg.Text("Agent: " + str(red_players['red2_character']))],
        [sg.Text("C Casts: " + str(red_players['red2_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red2_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red2_q_casts']))],
        [sg.Text("X Casts: " + str(red_players['red2_x_casts']))],
        [sg.Text("ACS: " + str(red_players['red2_score']))],
        [sg.Text("Kills: " + str(red_players['red2_kills']))],
        [sg.Text("Deaths: " + str(red_players['red2_deaths']))],
        [sg.Text("Assist: " + str(red_players['red2_assists']))],
        [sg.Text("H/S %: " + str(round(((red_players['red2_headshots']) / (red_players['red2_headshots']
                                                                           + red_players['red2_bodyshots'] +
                                                                           red_players[
                                                                               'red2_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(red_players['red2_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red2_damage_received']))]
    ]

    red3_tab = [
        [sg.Text("Level: " + str(red_players['red3_level']))],
        [sg.Text("Agent: " + str(red_players['red3_character']))],
        [sg.Text("C Casts: " + str(red_players['red3_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red3_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red3_q_casts']))],
        [sg.Text("X Casts: " + str(red_players['red3_x_casts']))],
        [sg.Text("ACS: " + str(red_players['red3_score']))],
        [sg.Text("Kills: " + str(red_players['red3_kills']))],
        [sg.Text("Deaths: " + str(red_players['red3_deaths']))],
        [sg.Text("Assist: " + str(red_players['red3_assists']))],
        [sg.Text("H/S %: " + str(round(((red_players['red3_headshots']) / (red_players['red3_headshots']
                                                                           + red_players['red3_bodyshots'] +
                                                                           red_players[
                                                                               'red3_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(red_players['red3_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red3_damage_received']))]
    ]

    red4_tab = [
        [sg.Text("Level: " + str(red_players['red4_level']))],
        [sg.Text("Agent: " + str(red_players['red4_character']))],
        [sg.Text("C Casts: " + str(red_players['red4_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red4_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red4_q_casts']))],
        [sg.Text("X Casts: " + str(red_players['red4_x_casts']))],
        [sg.Text("ACS: " + str(red_players['red4_score']))],
        [sg.Text("Kills: " + str(red_players['red4_kills']))],
        [sg.Text("Deaths: " + str(red_players['red4_deaths']))],
        [sg.Text("Assist: " + str(red_players['red4_assists']))],
        [sg.Text("H/S %: " + str(round(((red_players['red4_headshots']) / (red_players['red4_headshots']
                                                                           + red_players['red4_bodyshots'] +
                                                                           red_players[
                                                                               'red4_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(red_players['red4_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red4_damage_received']))]
    ]

    red5_tab = [
        [sg.Text("Level: " + str(red_players['red5_level']))],
        [sg.Text("Agent: " + str(red_players['red5_character']))],
        [sg.Text("C Casts: " + str(red_players['red5_c_casts']))],
        [sg.Text("E Casts: " + str(red_players['red5_e_cast']))],
        [sg.Text("Q Casts: " + str(red_players['red5_q_casts']))],
        [sg.Text("X Casts: " + str(red_players['red5_x_casts']))],
        [sg.Text("ACS: " + str(red_players['red5_score']))],
        [sg.Text("Kills: " + str(red_players['red5_kills']))],
        [sg.Text("Deaths: " + str(red_players['red5_deaths']))],
        [sg.Text("Assist: " + str(red_players['red5_assists']))],
        [sg.Text("H/S %: " + str(round(((red_players['red5_headshots']) / (red_players['red5_headshots']
                                                                           + red_players['red5_bodyshots'] +
                                                                           red_players[
                                                                               'red5_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(red_players['red5_damage_made']))],
        [sg.Text("Damage Received: " + str(red_players['red5_damage_received']))]
    ]

    blue1_tab = [
        [sg.Text("Level: " + str(blue_players['blue1_level']))],
        [sg.Text("Agent: " + str(blue_players['blue1_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue1_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue1_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue1_q_casts']))],
        [sg.Text("X Casts: " + str(blue_players['blue1_x_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue1_score']))],
        [sg.Text("Kills: " + str(blue_players['blue1_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue1_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue1_assists']))],
        [sg.Text("H/S %: " + str(round(((blue_players['blue1_headshots']) / (blue_players['blue1_headshots']
                                                                             + blue_players['blue1_bodyshots'] +
                                                                             blue_players[
                                                                                 'blue1_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue1_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue1_damage_received']))]
    ]

    blue2_tab = [
        [sg.Text("Level: " + str(blue_players['blue2_level']))],
        [sg.Text("Agent: " + str(blue_players['blue2_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue2_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue2_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue2_q_casts']))],
        [sg.Text("X Casts: " + str(blue_players['blue2_x_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue2_score']))],
        [sg.Text("Kills: " + str(blue_players['blue2_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue2_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue2_assists']))],
        [sg.Text("H/S %: " + str(round(((blue_players['blue2_headshots']) / (blue_players['blue2_headshots']
                                                                             + blue_players['blue2_bodyshots'] +
                                                                             blue_players[
                                                                                 'blue2_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue2_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue2_damage_received']))]
    ]

    blue3_tab = [
        [sg.Text("Level: " + str(blue_players['blue3_level']))],
        [sg.Text("Agent: " + str(blue_players['blue3_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue3_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue3_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue3_q_casts']))],
        [sg.Text("X Casts: " + str(blue_players['blue3_x_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue3_score']))],
        [sg.Text("Kills: " + str(blue_players['blue3_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue3_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue3_assists']))],
        [sg.Text("H/S %: " + str(round(((blue_players['blue3_headshots']) / (blue_players['blue3_headshots']
                                                                             + blue_players['blue3_bodyshots'] +
                                                                             blue_players[
                                                                                 'blue3_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue3_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue3_damage_received']))]
    ]

    blue4_tab = [
        [sg.Text("Level: " + str(blue_players['blue4_level']))],
        [sg.Text("Agent: " + str(blue_players['blue4_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue4_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue4_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue4_q_casts']))],
        [sg.Text("X Casts: " + str(blue_players['blue4_x_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue4_score']))],
        [sg.Text("Kills: " + str(blue_players['blue4_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue4_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue4_assists']))],
        [sg.Text("H/S %: " + str(round(((blue_players['blue4_headshots']) / (blue_players['blue4_headshots']
                                                                             + blue_players['blue4_bodyshots'] +
                                                                             blue_players[
                                                                                 'blue4_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue4_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue4_damage_received']))]
    ]

    blue5_tab = [
        [sg.Text("Level: " + str(blue_players['blue5_level']))],
        [sg.Text("Agent: " + str(blue_players['blue5_character']))],
        [sg.Text("C Casts: " + str(blue_players['blue5_c_casts']))],
        [sg.Text("E Casts: " + str(blue_players['blue5_e_cast']))],
        [sg.Text("Q Casts: " + str(blue_players['blue5_q_casts']))],
        [sg.Text("X Casts: " + str(blue_players['blue5_x_casts']))],
        [sg.Text("ACS: " + str(blue_players['blue5_score']))],
        [sg.Text("Kills: " + str(blue_players['blue5_kills']))],
        [sg.Text("Deaths: " + str(blue_players['blue5_deaths']))],
        [sg.Text("Assist: " + str(blue_players['blue5_assists']))],
        [sg.Text("H/S %: " + str(round(((blue_players['blue5_headshots']) / (blue_players['blue5_headshots']
                                                                             + blue_players['blue5_bodyshots'] +
                                                                             blue_players[
                                                                                 'blue5_legshots'])) * 100, 2)))],
        [sg.Text("Damage Dealt: " + str(blue_players['blue5_damage_made']))],
        [sg.Text("Damage Received: " + str(blue_players['blue5_damage_received']))]
    ]

    # defines the non-player specific data for the match
    metadata_layout = [
        [sg.Text("Map: " + metadata['map'][0])],
        [sg.Text("Game Start: " + metadata['game_start_patched'][0])],
        [sg.Text("Rounds Played: " + str(metadata['rounds_played'][0]))],
        [sg.Text("Server: " + metadata['cluster'][0])],

    ]

    # defines the red players tab group
    l_layout = [[sg.TabGroup([[sg.Tab((red_players['red1_name'] + " #" + red_players['red1_tag']),
                                      red1_tab, title_color='white'),
                               sg.Tab((red_players['red2_name'] + " #" + red_players['red2_tag']),
                                      red2_tab, title_color='white'),
                               sg.Tab((red_players['red3_name'] + " #" + red_players['red3_tag']),
                                      red3_tab, title_color='white'),
                               sg.Tab((red_players['red4_name'] + " #" + red_players['red4_tag']),
                                      red4_tab, title_color='white'),
                               sg.Tab((red_players['red5_name'] + " #" + red_players['red5_tag']),
                                      red5_tab, title_color='white')]],
                             title_color='red',
                             selected_title_color='white',
                             tab_location='lefttop'
                             )]
                ]

    # defines the blue players tab group
    r_layout = [[sg.TabGroup([[sg.Tab((blue_players['blue1_name'] + " #" + blue_players['blue1_tag']),
                                      blue1_tab, title_color='white'),
                               sg.Tab((blue_players['blue2_name'] + " #" + blue_players['blue2_tag']),
                                      blue2_tab, title_color='white'),
                               sg.Tab((blue_players['blue3_name'] + " #" + blue_players['blue3_tag']),
                                      blue3_tab, title_color='white'),
                               sg.Tab((blue_players['blue4_name'] + " #" + blue_players['blue4_tag']),
                                      blue4_tab, title_color='white'),
                               sg.Tab((blue_players['blue5_name'] + " #" + blue_players['blue5_tag']),
                                      blue5_tab, title_color='white')]],
                             title_color='blue',
                             selected_title_color='white',
                             tab_location='righttop',

                             )]
                ]

    # define the main layout using columns to centre data
    layout = [
        [sg.Column(metadata_layout, justification="c", element_justification="c")],
        [sg.Column(l_layout, justification="l", element_justification="c"),
         sg.Column(r_layout, justification="r", element_justification="c")]
    ]

    # defines the window and gives it a title and an icon
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    # this reads the event and the values provided from the window
    event, values = window.read()
    window.close()
    return event, values


def choice(option_choice, all_dicts, playername):
    """This function is used to call the specific function when the player
    decides which data they would like to request"""
    if option_choice == "Recent Match Overview":
        recent_match_summary_option(all_dicts, playername)
    elif option_choice == "Leader Board":
        leaderboard_option()
    elif option_choice == "Specific Match Breakdown":
        match_breakdown_option(all_dicts)


def leaderboard_display(dict):
    """This function takes the leaderboard dictionary and creates a sub list depending on the value
    of the slider element in the GUI """
    # defines the theme of the window
    sg.theme('DarkBlue')
    page = 1

    # this defines a subpage of the dictionary based on the pagenum parameter
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

    # This defines the layout using a Slider and many Text elements with keys.
    # This allow their values to be changed with .update()
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
        # this reads the event and the values provided from the window
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        pg_slider = int(values['slider'])
        pg = pg_slider
        window['slider'].update(50)
        window['slider'].update(1)
        # if the slider value does not match the current page number the text is updated
        if pg != page:
            players = pagedict(pg, dict)
            pagestart = (pg * 10) - 9
            pageend = (pg * 10)

            page = pg
            window['slider'].update(pg)
            window['text'].update(pg)

            # iterates through each key using f-strings and updates the values
            for i in range(0, 10):
                window[f'rank{i + 1}'].update(pagestart + i)
                window[f'name{i + 1}'].update(players[pagestart + i]["Name"][0])
                window[f'tag{i + 1}'].update(players[pagestart + i]["Tag"][0])
                window[f'wins{i + 1}'].update(players[pagestart + i]["Wins"][0])
                # some players choose to have their name and tag anonymous so if
                # no value is detected then "Anon" is outputted instead
                if players[pagestart + i]["Name"][0] == "" or players[pagestart + i]["Tag"][0] == "":
                    window[f'name{i + 1}'].update("Anon")
                    window[f'tag{i + 1}'].update("Anon")


# the main script that is run when the program is run
if __name__ == '__main__':
    # the local login using hashing
    main_login()
    # the gathering of the user RIOT detail and the request of their data from the API
    details = api_login()
    all_dicts = all_data(details[0], details[1])
    # main menu prompt
    popup("Close the main menu when you would like to select another option.")
    main_menu()
    # option choice window
    option_choice = option_menu()
    # user choice is passed to the choice() function along with their data
    choice(option_choice[0], all_dicts, details[0])
