import PySimpleGUI as sg
import pprint

from MainAPICall import getLeaderboard

leader_dict = getLeaderboard("eu", 1000)
print(leader_dict[1]["Name"][0])

pp = pprint.PrettyPrinter(sort_dicts=False)


def pagedict(pagenum, dictionary):
    pagestart = (pagenum * 10) - 9
    pageend = (pagenum * 10)
    sub_dict = {
        0: {
            "Name": ["test"],
            "Tag": ["123"],
            "Wins": ["---"]
        }
    }
    for i in range(pagestart, pageend + 1):
        print(i)
        sub_dict[i] = dictionary[i]

    pp.pprint(sub_dict)
    return sub_dict


# pagedict(1, leader_dict)


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
            print(i)
            sub_dict[i] = dictionary[i]

        pp.pprint(sub_dict)
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

            print(players)
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


leaderboard_display(leader_dict)
