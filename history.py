# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import var

def showHistory(transformator):
    # create theme
    sg.theme("DarkTeal11")

    # font
    font1 = ("Arial", 12, "bold")
    font2 = ("Arial", 12)
    font3 = ("Arial", 16, "bold")

    # sg.set_options(font=font1)
    sg.SetOptions(element_padding=((1, 1), 0))

    # layout for button
    LayoutButton = [
        [sg.Text(" ")],
        [
            sg.Button("Pilih Data", size=(17, 1), font=font1),
            sg.Combo(
                [name[0] for name in transformator],
                size=(15, 1),
                key="sample",
            ),
            sg.Button("Hapus Data", size=(12, 1), font=font1),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            sg.Text(" "),
            # Button Halaman
            sg.Button("Perhitungan", size=(10, 1), font=font1, key="btnPerhitungan"),
        ],
        # Penamaan Halaman
        [sg.Text(" ")],
        [
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("    "),
            sg.Text("Halaman History", size=(20, 1), justification="c", font=font3),
        ],
    ]

    # Data untuk tabel
    data = [
        [
            "Tansformator 1",
            "24-03-2022",
            "DPM",
            "7",
            "5",
            "9",
            "12",
            "24",
            "D1",
            "Titik X= 0.98765 dan Y=0.23456",
            "Sela Aulia",
        ],
        [
            "Tansformator 1",
            "23-03-2022",
            "DTM",
            " ",
            "5",
            "9",
            "12",
            " ",
            "D1",
            "Titik X= 0.98765 dan Y=0.23456",
            "Sela Aulia",
        ],
        [
            "Tansformator 1",
            "22-03-2022",
            "DPM",
            "7",
            "5",
            "9",
            "12",
            "24",
            "D1",
            "Titik X= 0.98765 dan Y=0.23456",
            "Sela Aulia",
        ],
        [
            "Tansformator 1",
            "21-03-2022",
            "DTM",
            " ",
            "5",
            "9",
            "12",
            " ",
            "D1",
            "Titik X= 0.98765 dan Y=0.23456",
            "Sela Aulia",
        ],
        [
            "Tansformator 1",
            "20-03-2022",
            "DPM",
            "7",
            "5",
            "9",
            "12",
            "24",
            "D1",
            "Titik X= 0.98765 dan Y=0.23456",
            "Sela Aulia",
        ],
    ]
    # Layout tabel
    table_layout = [
        [
            sg.Table(
                values=data,
                headings=[
                    "Transformator",
                    "Tanggal",
                    "Metode",
                    "H2",
                    "CH4",
                    "C2H2",
                    "C2H4",
                    "C2H6",
                    "Titik Kerusakan",
                    "Deskripsi",
                    "Penguji",
                ],
                num_rows=5,
                col_widths=[15, 5, 20],
                justification="c",
            )
        ]
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
                size=(45, 1),
                justification="c",
                font=font3,
            ),
        ],
        [sg.Text("  ")],
        # tampilan tabel
        table_layout,
        # Untuk tampilan layout bawah
        LayoutButton,
    ]

    # showing the window
    window = sg.Window("Identifikasi Kegagalan Transformator", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == "Select Data Sample":
            sampletr = values["sample"]
            if sampletr == "Transformers 1":
                window["cH2"].update("21")
                window["rH2"].update("0")
                window["cCH4"].update("39")
                window["rCH4"].update("0")
                window["cC2H2"].update("0")
                window["rC2H2"].update("0")
                window["cC2H4"].update("2")
                window["rC2H4"].update("0.401")
                window["cC2H6"].update("53")
                window["rC2H6"].update("8.699")

            if sampletr == "Transformers 2":  # BALONGBENDO 2, STATUS 2
                window["cH2"].update("85")
                window["rH2"].update("18.639")
                window["cCH4"].update("43")
                window["rCH4"].update("6.982")
                window["cC2H2"].update("0")
                window["rC2H2"].update("0")
                window["cC2H4"].update("2")
                window["rC2H4"].update("0.472")
                window["cC2H6"].update("55")
                window["rC2H6"].update("9.592")

            if sampletr == "Transformers 3":  # BAMBE 2, STATUS 3
                window["cH2"].update("33000")
                window["rH2"].update("21781.330")
                window["cCH4"].update("188000")
                window["rCH4"].update("124662.671")
                window["cC2H2"].update("0")
                window["rC2H2"].update("0")
                window["cC2H4"].update("221000")
                window["rC2H4"].update("145903.047")
                window["cC2H6"].update("132000")
                window["rC2H6"].update("87587.747")

        if event == "Clear Data":
            window["cH2"].update("")
            window["rH2"].update("")
            window["cCH4"].update("")
            window["rCH4"].update("")
            window["cC2H2"].update("")
            window["rC2H2"].update("")
            window["cC2H4"].update("")
            window["rC2H4"].update("")
            window["cC2H6"].update("")
            window["rC2H6"].update("")
        
        if event == "btnPerhitungan":
            window.close()

    #     #DPM
    #     #DPM PERCENTAGE

    # #     if event == 'DPM 1':

    window.close()
    return True