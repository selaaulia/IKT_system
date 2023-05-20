import PySimpleGUI as sg

# Membuat tampilan layout popup
layout = [
    [sg.Text('Masukkan Nama:'), sg.InputText(key='nama')],
    [sg.Text('Masukkan Usia:'), sg.InputText(key='usia')],
    [sg.Button('OK'), sg.Button('Batal')]
]

# Membuat tampilan window utama
main_layout = [
    [sg.Button('Tampilkan Popup')]
]

# Membuat objek window dari tampilan utama
window = sg.Window('Contoh Popup').Layout(main_layout)

# Looping event handler window utama
while True:
    event, values = window.Read()

    if event == 'Tampilkan Popup':
        # Membuat objek window dari layout popup
        popup = sg.Window('Contoh Popup').Layout(layout)

        # Looping event handler window popup
        while True:
            event, values = popup.Read()

            if event == 'OK':
                nama = values['nama']
                usia = values['usia']
                sg.Popup(f'Nama: {nama}\nUsia: {usia}')
                break

            if event == 'Batal' or event == sg.WIN_CLOSED:
                break

        popup.Close()

    if event == sg.WIN_CLOSED:
        break

window.Close()
