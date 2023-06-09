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
                key="transformator",
                enable_events=True,
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

    # Layout tabel
    table_layout = [
        [
            sg.Table(
                values=[],
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
                key="data",
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

        if event == "transformator":
            namatransformator = values["transformator"]
            for item in transformator:
                if namatransformator == item[0]:
                    idtransformator = item[1]
                    break
            response = var.getResult(idtransformator).json()
            table_data = [
                [
                    row["transformator"],
                    row["date"],
                    row["method"],
                    row["H2"],
                    row["CH4"],
                    row["C2H2"],
                    row["C2H4"],
                    row["C2H6"],
                    row["fault"],
                    row["description"],
                    row["penguji"],
                ]
                for row in response
            ]
            window["data"].update(values=table_data)

        if event == "btnPerhitungan":
            window.close()

    window.close()
    return True
