from threading import Thread
import PySimpleGUI as sg
import requests
#
#
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


def p2():
    print("2")
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=loading)
#     t2 = Thread(target=p2)
#     t1.start()
#     t2.start()
#     t1.join()  # Don't exit while threads are running
#     t2.join()
#


from multiprocessing import Process


if __name__ == '__main__':
    Process(target=loading).start()
    Process(target=p2).start()