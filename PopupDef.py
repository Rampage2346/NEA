import PySimpleGUI as sg


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

    window = sg.Window('Test', layout, modal=True, icon='valorant.ico').read(close=True)
    window.close()


popup("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer augue purus, gravida a tortor sit amet, \n"
      "pulvinar cursus massa. Cras ullamcorper pellentesque tortor, a aliquet nunc iaculis in. Nam lacus diam, \n"
      "lacinia et augue quis, iaculis imperdiet ipsum. Pellentesque ac purus nec erat ultricies finibus. Vestibulum \n"
      "consectetur augue at tellus ullamcorper consequat id sed sem. Cras rhoncus massa dolor, vitae pharetra mi \n"
      "facilisis at. Maecenas at dui dui. Donec condimentum, nisi non dignissim interdum, sem dui faucibus quam, \n"
      "quis pulvinar diam tellus at ligula. Suspendisse in rutrum eros.")
