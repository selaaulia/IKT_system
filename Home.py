# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import math
import numpy as np
import io
import requests
import json

# from Perhitungan import create_perhitungan
# from History import create_history

# create theme
sg.theme("DarkTeal11")

# font
font1 = ("Arial", 12, "bold")
font2 = ("Arial", 12)
font3 = ("Arial", 16, "bold")

# sg.set_options(font=font1)
sg.SetOptions(element_padding=((1, 1), 0))

# mengambil data penguji
data = requests.get("http://localhost:8000/api/penguji").json()
penguji = [(item["name"], item["id"]) for item in data]
data = requests.get("http://localhost:8000/api/transformator").json()
transformator = [(item["name"], item["id"]) for item in data]

# Layout 1 untuk identitas
layout1 = [
    # Judul Input Data Kandungan Konsentrasi Gas
    [
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text(
            "Identitas Penguji, Transformator, & Metode",
            size=(20, 2),
            justification="c",
            font=font3,
        ),
    ],
    # Input nama penguji
    [sg.Text("")],
    [
        sg.Text("Nama Penguji", size=(12, 1), justification="c", font=font2),
        sg.Combo(
            [name[0] for name in penguji],
            key="Nama_penguji",
            size=(20, 1),
            enable_events=True,
        ),
        sg.Text("  "),
        sg.Button("+ Penguji"),
    ],
    [sg.Text("     ")],
    # Input nama transformator
    [
        sg.Text("Nama Transformator", size=(12, 2), justification="c", font=font2),
        sg.Combo(
            [name[0] for name in transformator],
            key="Nama_transformator",
            size=(20, 1),
            enable_events=True,
        ),
        sg.Text("  "),
        sg.Button("+ Trafo"),
    ],
    [sg.Text("     ")],
    # Input metode perhitungan yang digunakan (DTM/DPM)
    [
        sg.Text("Metode", size=(12, 1), justification="c", font=font2),
        sg.Combo(["DTM", "DPM"], key="Metode", size=(20, 1), enable_events=True),
    ],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    #   Button Input (Digunakan untuk menmapilkan popup input nama transformator dan nama penguji baru)
    # [sg.Text('')],
    # [sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Text('  '),
    #  sg.Button('Input', size=(15,1), font=font1)],
    #  [sg.Text('')],
    # Keterangan
    [
        sg.Text(
            "Keterangan: \nButton +Penguji / +trafo digunakan untuk menambah nama penguji dan nama transformator yang belum terdapat pada list dropdown",
            size=(35, 4),
            background_color="#4a4740",
            text_color="white",
            justification="l",
            font=font2,
        )
    ],
]

# layout left
layout2_DPM = [
    # Judul Input Data Kandungan Konsentrasi Gas
    [sg.Text("Inputan Konsentrasi Gas", size=(20, 1), justification="c", font=font3)],
    [
        sg.Text(
            "Duval Pentagon Method (DPM)", size=(25, 1), justification="c", font=font1
        )
    ],
    [sg.Text("")],
    [
        sg.Text("Gas", size=(5, 1), justification="l", font=font1),
        sg.Text("Concentration (ppm)", size=(20, 1), justification="c", font=font1, key="gas"),
        #  sg.Text('Rate (ppm/year)',size=(15,1), justification='l', font=font1)
    ],
    [sg.Text("")],
    [
        sg.Text("H2", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dpm-H2", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rH2', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("CH4", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dpm-CH4", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rCH4', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("C2H2", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dpm-C2H2", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rC2H2', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("C2H4", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dpm-C2H4", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rC2H4', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("C2H6", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dpm-C2H6", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rC2H6', size=(14,1), justification='c')
    ],
    [sg.Text("  ")],
    # Buttom Analisis
    [sg.Text("             "), sg.Button("Analisis", size=(15, 1), font=font1, key="AnalisisDPM")],
    [sg.Text("")],
]

layout2_DTM = [  # Judul Input Data Kandungan Konsentrasi Gas
    [sg.Text("Inputan Konsentrasi Gas", size=(20, 1), justification="c", font=font3)],
    [
        sg.Text(
            "Duval Triagle Method (DTM)", size=(25, 1), justification="c", font=font1
        )
    ],
    [sg.Text("")],
    [
        sg.Text("Gas", size=(5, 1), justification="l", font=font1),
        sg.Text("Concentration (ppm)", size=(20, 1), justification="c", font=font1),
        #  sg.Text('Rate (ppm/year)',size=(15,1), justification='l', font=font1)
    ],
    [sg.Text("")],
    [
        sg.Text("CH4", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dtm-CH4", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rCH4', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("C2H2", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dtm-C2H2", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rC2H2', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [
        sg.Text("C2H4", size=(6, 1), justification="l", font=font2),
        sg.Text("     "),
        sg.InputText("", key="dtm-C2H4", size=(20, 1), justification="c"),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text('  '),
        #  sg.Text(''),
        #  sg.InputText('', key='rC2H4', size=(14,1), justification='c')
    ],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    [sg.Text("     ")],
    # Buttom Analisis
    [sg.Text("             "), sg.Button("Analisis", size=(15, 1), font=font1, key="AnalisisDTM")],
    [sg.Text("")],
]
# layout showing DGA Status based on the standard

layout3 = [
    # [sg.Text('     ')],
    [
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("Hasil Analisis", size=(20, 1), justification="c", font=font3),
    ],
    # Nama Penguji
    [sg.Text("  ")],
    [
        sg.Text("Nama Penguji", size=(8, 2), justification="1", font=font2),
        sg.Text("  "),
        sg.Text(
            "",
            size=(20, 2),
            key="result",
            background_color="lightgrey",
            text_color="black",
            justification="c",
        ),
    ],
    # Metode & Titik Kerusakan
    [sg.Text("  ")],
    [
        sg.Text("Metode", size=(8, 2), justification="1", font=font2),
        sg.Text("  "),
        sg.Text(
            "",
            size=(8, 2),
            key="result",
            background_color="lightgrey",
            text_color="black",
            justification="c",
        ),
        sg.Text("  "),
        sg.Text("Titik Kerusakan", size=(8, 2), justification="c", font=font2),
        sg.Text("  "),
        sg.Text(
            "",
            size=(8, 2),
            key="result",
            background_color="lightgrey",
            text_color="black",
            justification="c",
        ),
        sg.Text("  "),
    ],
    # Deskripsi Hasil titik kerusakan
    [sg.Text("  ")],
    [
        sg.Text("Deskripsi", size=(8, 1), justification="c", font=font2),
        sg.Text("  "),
        sg.Text(
            "",
            size=(30, 5),
            key="result",
            background_color="lightgrey",
            text_color="black",
            justification="c",
        ),
        sg.Text("  "),
    ],
    # Penamaan
    [sg.Text("  ")],
    [
        sg.Text(
            "Sela Aulia Siswanto \nTeknik Informatika \nPoliteknik Negeri Malang \nEkojono, ST,. M.Kom. \n© 2023",
            size=(30, 5),
            background_color="#4a4740",
            text_color="white",
            justification="l",
            font=font2,
        )
    ],
]

# layout for button
LayoutButton = [
    # Penamaan Halaman
    [sg.Text(" ")],
    [
        sg.Text("    "),
        sg.Text("    "),
        sg.Text("Halaman Perhitungan", size=(70, 1), justification="c", font=font3),
    ],
    # Button Halaman
    [
        sg.Text("                                              "),
        sg.Text("                                              "),
        sg.Text(" "),
        sg.Button("Perhitungan", size=(10, 1), font=font1),
        sg.Button("History", size=(10, 1), font=font1),
    ],
]

# main layout
layout = [
    # [sg.Text('', size=(25,1), justification='c', font=font3),
    [sg.Text(" ")],
    [
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text("  "),
        sg.Text(
            "Identifikasi Kegagalan Transformator Dengan DTM DPM",
            size=(65, 1),
            justification="c",
            font=font3,
        ),
    ],
    [sg.Text("  ")],
    [
        sg.Frame("", layout1, font=font1),
        sg.Frame("", layout2_DPM, font=font2, key="layout2DPM", visible=False),
        sg.Frame("", layout2_DTM, font=font2, key="layout2DTM", visible=False),
        sg.Frame("", layout3, font=font2, key="hasil"),
    ],
    LayoutButton,
]

# Membuat Tampilan Popup Input Nama Penguji dan Nama Transformator
Layout_Popup_Penguji = [
    [sg.Text("Masukkan nama penguji:")],
    [sg.Input(key="Nama_penguji")],
    [sg.Text(" ")],
    [sg.Button("OK"), sg.Button("Batal")],
]
Layout_Popup_Transformator = [
    [sg.Text("Masukkan nama transformator:")],
    [sg.Input(key="Nama_transformator")],
    [sg.Text(" ")],
    [sg.Button("OK"), sg.Button("Batal")],
]


# showing the window
window = sg.Window("Identifikasi Kegagalan Transformator", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # # Button untuk pindah Halaman
    # if event == 'Perhitungan':
    #     window.close()  # Tutup window saat ini
    #     window = sg.Window('Multi-Layout')  # Buka window baru
    #     window.Layout = create_perhitungan()  # Set layout Halaman 2 - Tampilan A
    #     current_layout = 'Perhitungan'

    # elif event == 'History' and current_layout == 'layout2_b':
    #       window.close()  # Tutup window saat ini
    #       window = sg.Window('Multi-Layout')  # Buka window baru
    #       window.Layout = create_history()  # Set layout Halaman 2 - Tampilan A
    #       current_layout = 'History'

    if event == "Metode":
        window['hasil'].update(visible=False)
        metode = values["Metode"]
        if metode == "DTM":
            window["layout2DPM"].update(visible=False)
            window['layout2DTM'].update(visible=True)
        elif metode == "DPM":
            window["layout2DPM"].update(visible=True)
            window['layout2DTM'].update(visible=False)
        window['hasil'].update(visible=True)
        window.refresh()

    # Bagian Popup (Untuk input nama penguji)
    if event == "+ Penguji":
        # Membuat objek window dari layout popup
        popup = sg.Window("Input Nama Penguji").Layout(Layout_Popup_Penguji)

        # Looping event handler window popup
        while True:
            event, values = popup.Read()

            if event == "OK":
                Nama_penguji = values["Nama_penguji"]
                # sg.Popup(f'Nama Penguji: {Nama_penguji}')
                data = {"name": Nama_penguji}
                response = requests.post("http://localhost:8000/api/penguji", json=data)
                if response.status_code == 200:
                    sg.Popup(response.text)
                break

            if event == "Batal" or event == sg.WIN_CLOSED:
                break

        popup.Close()

    # Bagian Popup (Untuk input nama transformator)
    if event == "+ Trafo":
        # Membuat objek window dari layout popup
        popup = sg.Window("Input Nama Transformator").Layout(Layout_Popup_Transformator)

        # Looping event handler window popup
        while True:
            event, values = popup.Read()

            if event == "OK":
                Nama_transformator = values["Nama_transformator"]
                # sg.Popup(f'Nama Transformator: {Nama_transformator}')
                data = {"name": Nama_transformator}
                response = requests.post(
                    "http://localhost:8000/api/transformator", json=data
                )
                if response.status_code == 200:
                    sg.Popup(response.text)
                break

            if event == "Batal" or event == sg.WIN_CLOSED:
                break

        popup.Close()

    # Kirim data input DTM dan DPM ke database untuk analisis
    if event == "AnalisisDTM" or event == "AnalisisDPM":
        # Input_DTM = values["Input_DTM"]
        # Mendapatkan Id nama penguji
        namapenguji = values['Nama_penguji']
        for item in penguji:
            if namapenguji == item[0]:
                idpenguji = item[1]

        # Mendapatkan Id nama transformator
        namatransformator = values['Nama_transformator']
        for item in transformator:
            if namatransformator == item[0]:
                idtransformator = item[1]
        
        if event == 'AnalisisDTM':
            ch4 = values['dtm-CH4']
            c2h2 = values['dtm-C2H2']
            c2h4 = values['dtm-C2H4']
            data = {
                "penguji_id": idpenguji, 
                "transformator_id": idtransformator,
                "CH4": ch4,
                "C2H2": c2h2,
                "C2H4": c2h4
                }
            response = requests.post("http://localhost:8000/api/input-dtm", json=data)
            if response.status_code == 200:
                sg.Popup(response.text)

        if event == 'AnalisisDPM':
            h2 = values['dpm-H2']
            ch4 = values['dpm-CH4']
            c2h2 = values['dpm-C2H2']
            c2h4 = values['dpm-C2H4']
            c2h6 = values['dpm-C2H6']
            data = {
                "penguji_id": idpenguji, 
                "transformator_id": idtransformator,
                "H2": h2,
                "CH4": ch4,
                "C2H2": c2h2,
                "C2H4": c2h4,
                "C2H6": c2h6
                }
            response = requests.post("http://localhost:8000/api/input-dpm", json=data)
            if response.status_code == 200:
                sg.Popup(response.text)
        # data = {"penguji_id": Input_DTM}, {"transformator_id": Input_DTM}, {"CH4": Input_DTM}



window.close()
