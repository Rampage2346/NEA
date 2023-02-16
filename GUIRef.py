import PySimpleGUI as pg

"""
    Demo - Element List

    All elements shown in 1 window as simply as possible.

    Copyright 2022 PySimpleGUI
"""

use_custom_titlebar = True if pg.running_trinket() else False


def make_window(theme=None):
    name_size = 23

    def name(name):
        dots = name_size - len(name) - 2
        return pg.Text(name + ' ' + '•' * dots, size=(name_size, 1), justification='r', pad=(0, 0), font='Courier 10')

    pg.theme(theme)

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = pg.MenubarCustom
    else:
        Menu = pg.Menu

    treedata = pg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [
        [name('Text'), pg.Text('Text')],
        [name('Input'), pg.Input(s=15)],
        [name('Multiline'), pg.Multiline(s=(15, 2))],
        [name('Output'), pg.Output(s=(15, 2))],
        [name('Combo'),
         pg.Combo(pg.theme_list(), default_value=pg.theme(), s=(15, 22), enable_events=True, readonly=True,
                  k='-COMBO-')],
        [name('OptionMenu'), pg.OptionMenu(['OptionMenu', ], s=(15, 2))],
        [name('Checkbox'), pg.Checkbox('Checkbox')],
        [name('Radio'), pg.Radio('Radio', 1)],
        [name('Spin'), pg.Spin(['Spin', ], s=(15, 2))],
        [name('Button'), pg.Button('Button')],
        [name('ButtonMenu'), pg.ButtonMenu('ButtonMenu', pg.MENU_RIGHT_CLICK_EDITME_EXIT)],
        [name('Slider'), pg.Slider((0, 10), orientation='h', s=(10, 15))],
        [name('Listbox'), pg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True, s=(15, 2))],
        [name('Image'), pg.Image(pg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
        [name('Graph'), pg.Graph((125, 50), (0, 0), (125, 50), k='-GRAPH-')]]

    layout_r = [
        [name('Canvas'), pg.Canvas(background_color=pg.theme_button_color()[1], size=(125, 40))],
        [name('ProgressBar'), pg.ProgressBar(100, orientation='h', s=(10, 20), k='-PBAR-')],
        [name('Table'), pg.Table([[1, 2, 3], [4, 5, 6]], ['Col 1', 'Col 2', 'Col 3'], num_rows=2)],
        [name('Tree'), pg.Tree(treedata, ['Heading', ], num_rows=3)],
        [name('Horizontal Separator'), pg.HSep()],
        [name('Vertical Separator'), pg.VSep()],
        [name('Frame'), pg.Frame('Frame', [[pg.T(s=15)]])],
        [name('Column'), pg.Column([[pg.T(s=15)]])],
        [name('Tab, TabGroup'), pg.TabGroup([[pg.Tab('Tab1', [[pg.T(s=(15, 2))]]), pg.Tab('Tab2', [[]])]])],
        [name('Pane'), pg.Pane([pg.Col([[pg.T('Pane 1')]]), pg.Col([[pg.T('Pane 2')]])])],
        [name('Push'), pg.Push(), pg.T('Pushed over')],
        [name('VPush'), pg.VPush()],
        [name('Sizer'), pg.Sizer(1, 1)],
        [name('StatusBar'), pg.StatusBar('StatusBar')],
        [name('Sizegrip'), pg.Sizegrip()]
    ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [pg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c',
                    expand_x=True)],
              [pg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True,
                           k='-USE CUSTOM TITLEBAR-', p=0)],
              [pg.Col(layout_l, p=0), pg.Col(layout_r, p=0)]]

    window = pg.Window('The PySimpleGUI Element List', layout, finalize=True,
                       right_click_menu=pg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True,
                       use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30)  # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=pg.EMOJI_BASE64_HAPPY_JOY,
                                 location=(0, 50))  # Draw something in the Graph Element

    return window


window = make_window()

while True:
    event, values = window.read()
    # sg.Print(event, values)
    if event == pg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        pg.execute_editor(__file__)
    if values['-COMBO-'] != pg.theme():
        pg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        pg.set_options(use_custom_titlebar=use_custom_titlebar)
        window.close()
        window = make_window()
    elif event == 'Version':
        pg.popup_scrolled(pg.get_versions(), __file__, keep_on_top=True, non_blocking=True)
window.close()
