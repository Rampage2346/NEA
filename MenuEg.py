import PySimpleGUI as pg

pg.theme('DarkBlue')
pg.set_options(element_padding=(0, 0))

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ GUI Defintion ------ #
layout = [
    [pg.Menu(menu_def, )],
    [pg.Output(size=(60, 20))]
]

window = pg.Window("Main Menu EG", layout, default_element_size=(12, 1), auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(12, 1))

# ------ Loop & Process button menu choices ------ #
while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == 'Exit':
        break
    print('Button = ', event)

    # ------ Process menu choices ------ #
    if event == 'About...':
        pg.popup('MetaTrak', 'Version 1.0', 'Made Using PySimpleGUI')
    elif event == 'Open':
        filename = pg.popup_get_file('file to open', no_window=True)
        print(filename)