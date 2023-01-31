import PySimpleGUI as pg


def popup(message):
    pg.theme('DarkBlue')
    layout = [
        [pg.Text(message)],
        [pg.Push(), pg.Button('OK')],
    ]
    pg.Window('Test', layout, modal=True).read(close=True)


popup("sdfjasldfgj")

