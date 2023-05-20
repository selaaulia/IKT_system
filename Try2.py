import PySimpleGUI as sg

layout = [
    [sg.Frame("Frame 1", [[sg.Text("Konten Frame 1")]], key="-FRAME1-")],
    [sg.Frame("Frame 2", [[sg.Text("Konten Frame 2")]], key="-FRAME2-")],
    [sg.Button("Sembunyikan Frame 1"), sg.Button("Tampilkan Frame 1")],
]

window = sg.Window("Contoh", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Sembunyikan Frame 1":
        window["-FRAME1-"].hide_row()
    elif event == "Tampilkan Frame 1":
        window["-FRAME1-"].unhide_row()

window.close()
