import PySimpleGUI as sg
import requests
from PIL import Image
import io

cat_bytes = requests.get("https://placekitten.com/200/300")
cat_image = Image.open(io.BytesIO(cat_bytes.content))
cat_png = io.BytesIO()
cat_image.save(cat_png, format="PNG")
cat_display = cat_png.getvalue()

layout = [
    [sg.Image(data=cat_display)],
    [sg.Button('Exit')]
]
window = sg.Window("Clock with cat image", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
