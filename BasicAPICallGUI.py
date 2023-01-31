import PySimpleGUI as pg
import json
import requests
# import os
from PIL import Image
import io
import pprint


def popupwithimage(message):
    layout = [
        [pg.Image(data=card_display)],
        [pg.Text(message)],
        [pg.Push(), pg.Button('OK')],
    ]
    pg.Window('Account Details', layout, modal=True).read(close=True)


def popup(message):
    layout = [
        [pg.Canvas()],
        [pg.Text(message)],
        [pg.Push(), pg.Button('OK')],
    ]
    pg.Window('Account Details', layout, modal=True).read(close=True)


def inputWindow():
    layout = [
        [pg.Text('Enter Your Riot ID')],
        [pg.InputText()],
        [pg.Text('Enter Your Tagline')],
        [pg.InputText()],
        [pg.Button('Submit'), pg.Button('Cancel')]
    ]
    inpwindow = pg.Window('Riot API Call', layout)
    return inpwindow


def mainMenu():
    layout = [
        [pg.Button('Submit1'), pg.Canvas(), pg.Button('Submit2')],
        [pg.Canvas(), pg.Canvas(), pg.Canvas()],
        [pg.Canvas(), pg.Canvas(), pg.Canvas()],
        [pg.Button('Submit3'), pg.Canvas(), pg.Button('Cancel')]
    ]
    mainwindow = pg.Window('Test Menu', layout)
    return mainwindow


def playerInfo(ID, tagline):
    response_API = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_API.status_code
    data = response_API.text
    raw = json.loads(data)
    pprint.pprint(raw)

    userID = raw['data']['name']
    accountlvl = raw['data']['account_level']
    region = raw['data']['region']
    uregion = region.upper()
    IDcode = raw['data']['card']['wide']
    puuid = raw['data']['puuid']
    uregion = region.upper()

    return userID, accountlvl, uregion, IDcode, puuid


# set theme
pg.theme('DarkBlue')
# create layout

start = True
# event loop
while True:
    # inputWindow()
    if start == True:
        event1, values1 = mainMenu().read()
        start = True

    # event, values = inputWindow().read()

    # if event == 'Cancel' or event == pg.WINDOW_CLOSED:
    #     break

    if event1 == 'Cancel' or event1 == pg.WINDOW_CLOSED:
        break
    elif event1 == 'Submit1':

        event, values = inputWindow().read()

        if event == 'Cancel' or event == pg.WINDOW_CLOSED:
            break

        name = values[0]
        tag = values[1]
        print(values[0], values[1])

        allDetails = []
        allDetails = playerInfo(name, tag)
        print(allDetails)

        playerID = allDetails[0]
        playerTag = allDetails[1]
        playerReg = allDetails[2]
        IDforURL = allDetails[3]

        card_bytes = requests.get(IDforURL)

        card_image = Image.open(io.BytesIO(card_bytes.content))
        card_png = io.BytesIO()
        card_image.save(card_png, format="PNG")
        card_display = card_png.getvalue()

        # print(card_bytes)
        # print(card_image)
        # print(card_png)
        # print(card_display)

        popupwithimage(f'Account Name: {allDetails[0]} \n\nAccount Level: {allDetails[1]} \n\nAccount Region: {allDetails[2]}')
        # break
    elif event1 == 'Submit2':
        popup("Submit2")
    elif event1 == 'Submit3':
        popup("Submit3")

# close window
inputWindow().close()
mainMenu().close()
