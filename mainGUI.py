import PySimpleGUI as sg
import pprint
import requests
from PIL import Image
import io
from login import login_cred_check, new_user_append
from MainAPICall import allPlayerData, getLeaderboard, format_rr

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
    print(login_choice)

    if login_choice[0] == "I already have an account":
        check = False
        login_inp_array = login_window()
        if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        print(login_inp_array)
        check = login_cred_check(login_inp_array[1][0], login_inp_array[1][1])
        print(check)
        while check is False:
            popup("Incorrect Username or Password!\nPlease try again.")
            login_inp_array = login_window()
            if login_inp_array[0] == 'Cancel' or login_inp_array[0] == sg.WINDOW_CLOSED:
                exit()
            print(login_inp_array)
            check = login_cred_check(login_inp_array[1][0], login_inp_array[1][1])
            print(check)

    elif login_choice[0] == "I am a new user":
        new_user_inp_array = new_user_window()
        if new_user_inp_array[0] == 'Cancel' or new_user_inp_array[0] == sg.WINDOW_CLOSED:
            exit()
        print(new_user_inp_array)
        new_user_append(new_user_inp_array[1][0], new_user_inp_array[1][1])


def api_login():
    popup("You have now logged in or created your new account. Now you will need to provide the Valorant account \n"
          "that you would like to fetch the stats for. This means your IGN and your tagline, the string after the #.\n")
    api_inp_array = api_login_window()
    return api_inp_array[1][0], api_inp_array[1][1]


def leaderboard_inp_window():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Enter the number of players you would like to display:')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()

    return event, values


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

    # layout_l = [
    #     [sg.Column(main_details, justification='c')],
    #     [sg.Column([[rank]], justification='c')],
    #     [sg.Column(rank_curr, justification='c')],
    #     [sg.Text(f"{ranking_in_tier} "), sg.Column(progress_bar), sg.Text("100")]
    # ]

    layout_l = [
        [sg.Text("Name: " + name), sg.Text("Level: " + account_level), sg.Text(region)],
        [sg.Text("Current Rank:")],
        [sg.Column([[rank]], justification='c')],
        [sg.Text(current_rank, justification='c')],
        [sg.Text(f"{ranking_in_tier} "), sg.Column(progress_bar), sg.Text("100")]
    ]

    ct1 = mmr_history[1]["current_tier"][0]
    mmr1 = mmr_history[1]["mmr_change"][0]
    ct2 = mmr_history[2]["current_tier"][0]
    mmr2 = mmr_history[2]["mmr_change"][0]
    ct3 = mmr_history[3]["current_tier"][0]
    mmr3 = mmr_history[3]["mmr_change"][0]

    format_rr()

    m1 = sg.Text(ct1), sg.Text(mmr1)
    m2 = sg.Text(ct2), sg.Text(mmr2)
    m3 = sg.Text(ct3), sg.Text(mmr3)

    layout_r = [
        [sg.Text("Match Overview")],
        [sg.Canvas()],
        [m1, m2, m3]
    ]

    layout_main = [
        [card],
        [sg.HorizontalSeparator()],
        [sg.Column(layout_l, element_justification='c', justification='c')],
        [sg.HorizontalSeparator()],
        [sg.Push(), layout_r]
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
    global all_dicts, account_data, mmr_data, mmr_history, region_version, leaderboard, match_id, last_match_data
    all_dicts = allPlayerData(name, id)
    account_data = all_dicts[0]
    mmr_data = all_dicts[1]
    mmr_history = all_dicts[2]
    region_version = all_dicts[3]
    match_id = all_dicts[4]
    last_match_data = all_dicts[5]


def option_menu():
    layout = [
        [sg.Button('Submit1'), sg.Canvas(), sg.Button('Submit2')],
        [sg.Canvas(), sg.Canvas(), sg.Canvas()],
        [sg.Canvas(), sg.Canvas(), sg.Canvas()],
        [sg.Button('Submit3'), sg.Canvas(), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event, values = window.read()
    window.close()

    return event, values


if __name__ == '__main__':
    # main_login()
    details = api_login()
    all_data(details[0], details[1])
    # loading()
    main_menu()

    # leader_data = leaderboard_inp_window()
    # print(leader_data)
    # getLeaderboard("eu", int(leader_data[1][0]))

# def all_data(name, id):
#     global all_dicts, account_data, mmr_data, mmr_history, region_version, leaderboard, match_id, last_match_data
#     all_dicts = allPlayerData(name, id)
#     account_data = all_dicts[0]
#     mmr_data = all_dicts[1]
#     mmr_history = all_dicts[2]
#     region_version = all_dicts[3]
#     match_id = all_dicts[4]
#     last_match_data = all_dicts[5]
#
#
# def main():
#     # main_login()
#     details = api_login()
#     all_data(details[0], details[1])
#     loading()
#     main_menu()
