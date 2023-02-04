import PySimpleGUI as sg
from login import login_cred_check, new_user_append
from MainAPICall import allPlayerData


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
        [sg.Canvas(), sg.Text("Please Choose an Option:"), sg.Canvas()],
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
    all_data(api_inp_array[1][0], api_inp_array[1][1])


def all_data(name, id):
    all_dicts = allPlayerData(name, id)
    account_data = all_dicts[0]
    mmr_data = all_dicts[1]
    mmr_history = all_dicts[2]
    region_version = all_dicts[3]
    leaderboard = all_dicts[4]
    match_id = all_dicts[5]
    last_match_data = all_dicts[6]


def main():
    main_login()
    api_login()

    # all_data()


main()
