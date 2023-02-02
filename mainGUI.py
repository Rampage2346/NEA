import PySimpleGUI as sg
from login import login_cred_check


def login_or_adduser():
    layout = [
        [sg.Text("Please Choose an Option:"), sg.Canvas()],
        [sg.Button("I already have an account"), sg.Button("I am a new user"), sg.Canvas()]

    ]
    window = sg.Window("MetaTrak", layout, size=(300, 75))
    event = window.read()
    window.close()

    return event


def login_window():
    layout = [
        [sg.Text('Enter Your Username')],
        [sg.InputText()],
        [sg.Text('Enter Your Password')],
        [sg.InputText()],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    window = sg.Window("MetaTrak", layout)
    event, values = window.read()
    window.close()

    return event, values


def main():
    login_choice = login_or_adduser()
    print(login_choice)
    if login_choice[0] == "I already have an account":
        login_inp_array = login_window()
        login_cred_check(login_inp_array[0], login_inp_array[1])
        print(login_inp_array)


    elif login_choice[0] == "I am a new user":
        print("test")


main()
