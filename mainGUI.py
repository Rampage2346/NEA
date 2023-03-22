import PySimpleGUI as sg
import pprint
import requests
from PIL import Image
import io
from login import login_cred_check, new_user_append
from MainAPICall import allPlayerData, format_rr, getLeaderboard

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

    ct1 = mmr_history[1]["current_tier"][0]
    mmr1 = mmr_history[1]["mmr_change"][0]
    ct2 = mmr_history[2]["current_tier"][0]
    mmr2 = mmr_history[2]["mmr_change"][0]
    ct3 = mmr_history[3]["current_tier"][0]
    mmr3 = mmr_history[3]["mmr_change"][0]

    rr_array = [mmr1, mmr2, mmr3]
    main = format_rr(rr_array)
    print(main)

    m1 = sg.Text(ct1), sg.Text(main[0])
    m2 = sg.Text(ct2), sg.Text(main[1])
    m3 = sg.Text(ct3), sg.Text(main[2])

    layout_main = [
        [card],
        [sg.HorizontalSeparator()],
        [sg.Column(layout_l, element_justification='c', justification='c')],
        [sg.HorizontalSeparator()],
        [sg.Text("Match Overview")],
        [sg.Canvas()],
        [sg.Push(), m1],
        [sg.Push(), m2],
        [sg.Push(), m3]
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


def recent_match_summary_option():
    pass


def leaderboard_option():
    leader_dict = getLeaderboard("eu", 1000)
    pp.pprint(leader_dict)
    leaderboard_display(leader_dict)


def match_breakdown_option():
    pass


def choice(option_choice):
    if option_choice == "Recent Match Overview":
        recent_match_summary_option()
    elif option_choice == "Leader Board":
        leaderboard_option()
    elif option_choice == "Specific Match Breakdown":
        match_breakdown_option()


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

    layout = [[sg.Slider(range=(1, 100), orientation='h', size=(10, 20), change_submits=True, key='slider'),
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

            window['rank1'].update(pagestart)
            window['name1'].update(players[pagestart]["Name"][0])
            window['tag1'].update(players[pagestart]["Tag"][0])
            window['wins1'].update(players[pagestart]["Wins"][0])
            if players[pagestart]["Name"][0] == "" or players[pagestart]["Tag"][0] == "":
                window['name1'].update("Anon")
                window['tag1'].update("Anon")

            window['rank2'].update(pagestart + 1)
            window['name2'].update(players[pagestart + 1]["Name"][0])
            window['tag2'].update(players[pagestart + 1]["Tag"][0])
            window['wins2'].update(players[pagestart + 1]["Wins"][0])
            if players[pagestart + 1]["Name"][0] == "" or players[pagestart + 1]["Tag"][0] == "":
                window['name2'].update("Anon")
                window['tag2'].update("Anon")

            window['rank3'].update(pagestart + 2)
            window['name3'].update(players[pagestart + 2]["Name"][0])
            window['tag3'].update(players[pagestart + 2]["Tag"][0])
            window['wins3'].update(players[pagestart + 2]["Wins"][0])
            if players[pagestart + 2]["Name"][0] == "" or players[pagestart + 2]["Tag"][0] == "":
                window['name3'].update("Anon")
                window['tag3'].update("Anon")

            window['rank4'].update(pagestart + 3)
            window['name4'].update(players[pagestart + 3]["Name"][0])
            window['tag4'].update(players[pagestart + 3]["Tag"][0])
            window['wins4'].update(players[pagestart + 3]["Wins"][0])
            if players[pagestart + 3]["Name"][0] == "" or players[pagestart + 3]["Tag"][0] == "":
                window['name4'].update("Anon")
                window['tag4'].update("Anon")

            window['rank5'].update(pagestart + 4)
            window['name5'].update(players[pagestart + 4]["Name"][0])
            window['tag5'].update(players[pagestart + 4]["Tag"][0])
            window['wins5'].update(players[pagestart + 4]["Wins"][0])
            if players[pagestart + 4]["Name"][0] == "" or players[pagestart + 4]["Tag"][0] == "":
                window['name5'].update("Anon")
                window['tag5'].update("Anon")

            window['rank6'].update(pagestart + 5)
            window['name6'].update(players[pagestart + 5]["Name"][0])
            window['tag6'].update(players[pagestart + 5]["Tag"][0])
            window['wins6'].update(players[pagestart + 5]["Wins"][0])
            if players[pagestart + 5]["Name"][0] == "" or players[pagestart + 5]["Tag"][0] == "":
                window['name6'].update("Anon")
                window['tag6'].update("Anon")

            window['rank7'].update(pagestart + 6)
            window['name7'].update(players[pagestart + 6]["Name"][0])
            window['tag7'].update(players[pagestart + 6]["Tag"][0])
            window['wins7'].update(players[pagestart + 6]["Wins"][0])
            if players[pagestart + 6]["Name"][0] == "" or players[pagestart + 6]["Tag"][0] == "":
                window['name7'].update("Anon")
                window['tag7'].update("Anon")

            window['rank8'].update(pagestart + 7)
            window['name8'].update(players[pagestart + 7]["Name"][0])
            window['tag8'].update(players[pagestart + 7]["Tag"][0])
            window['wins8'].update(players[pagestart + 7]["Wins"][0])
            if players[pagestart + 6]["Name"][0] == "" or players[pagestart + 6]["Tag"][0] == "":
                window['name8'].update("Anon")
                window['tag8'].update("Anon")

            window['rank9'].update(pagestart + 8)
            window['name9'].update(players[pagestart + 8]["Name"][0])
            window['tag9'].update(players[pagestart + 8]["Tag"][0])
            window['wins9'].update(players[pagestart + 8]["Wins"][0])
            if players[pagestart + 8]["Name"][0] == "" or players[pagestart + 8]["Tag"][0] == "":
                window['name9'].update("Anon")
                window['tag9'].update("Anon")

            window['rank10'].update(pagestart + 9)
            window['name10'].update(players[pagestart + 9]["Name"][0])
            window['tag10'].update(players[pagestart + 9]["Tag"][0])
            window['wins10'].update(players[pagestart + 9]["Wins"][0])
            if players[pagestart + 9]["Name"][0] == "" or players[pagestart + 9]["Tag"][0] == "":
                window['name10'].update("Anon")
                window['tag10'].update("Anon")


if __name__ == '__main__':
    # main_login()

    details = api_login()
    all_data(details[0], details[1])
    # loading()

    popup("Close the main menu when you would like to select another option.")
    main_menu()
    option_choice = option_menu()

    print(option_choice[0])
    choice(option_choice[0])

    # leader_data = leaderboard_inp_window()
    # print(leader_data)
    # getLeaderboard("eu", int(leader_data[1][0]))
