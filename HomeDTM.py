# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import math
import numpy as np
import io

#create theme
sg.theme('DarkTeal11')

#font
font1 = ("Arial", 12, 'bold')
font2 = ("Arial", 12)
font3 = ("Arial", 16, 'bold')

# sg.set_options(font=font1)
sg.SetOptions(element_padding=((1,1),0))

#Layout 1 untuk identitas
layout1 = [
            # Judul Input Data Kandungan Konsentrasi Gas
            [sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('Identitas Penguji, Transformator, & Metode', size=(20,2), justification='c', font=font3)], 

        #Input nama penguji
          [sg.Text('')],          
          [sg.Text('Nama Penguji', size=(12,1), justification='c', font=font2),
           sg.Combo(['Sela', 'Aulia'], key='Nama_penguji', size=(20,1), enable_events=True),
           sg.Text('  '),
           sg.Button('Submit'),
           sg.Text('  '),
           sg.Text('  ')],
          [sg.Text('     ')],

        #Input nama transformator
          [sg.Text('Nama Transformator', size=(12,2), justification='c', font=font2),
           sg.Combo(['Transformator 1', 'Transformator 2'], key='Nama_transformator', size=(20,1), enable_events=True),
           sg.Text('  '),
           sg.Button('Submit'),
           sg.Text('  '),
           sg.Text('  ')],
          [sg.Text('     ')],

        #Input metode perhitungan yang digunakan (DTM/DPM)
          [sg.Text('Metode', size=(12,1), justification='c', font=font2),
          sg.Combo(['DTM', 'DPM'], key='Metode', size=(20,1), enable_events=True),
          sg.Text('  '),
          sg.Button('Submit'),
          sg.Text('  '),
          sg.Text('  ')],
          [sg.Text('     ')],

        #   Button Input (Digunakan untuk menmapilkan popup input nama transformator dan nama penguji baru)
          [sg.Text('')],
          [sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Button('Input', size=(15,1), font=font1)],
           [sg.Text('')],

        # Keterangan
           [sg.Text('Keterangan: \nButton input digunakan untuk menginputkan \nnama penguji dan nama transformator yang belum terdapat pada list dropdown',size=(35,4),background_color='#4a4740', text_color='white',justification='l',font=font2)]
    ]

#layout left
layout2 = [
            # Judul Input Data Kandungan Konsentrasi Gas
            [sg.Text('Inputan Konsentrasi Gas', size=(20,1), justification='c', font=font3)],
            [sg.Text('Duval Triagle Method (DTM)',size=(25,1), justification='c', font=font1)],

          [sg.Text('')],
          [sg.Text('Gas', size=(5,1), justification='l', font=font1),
           sg.Text('Concentration (ppm)', size=(20,1), justification='c', font=font1),
          #  sg.Text('Rate (ppm/year)',size=(15,1), justification='l', font=font1)
          ],
          [sg.Text('')],
          
          [sg.Text('CH4', size=(6,1), justification='l', font=font2),
           sg.Text('     '),
           sg.InputText('', key='cCH4', size=(20,1), justification='c'),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text(''),
          #  sg.InputText('', key='rCH4', size=(14,1), justification='c')
           ],
          [sg.Text('     ')],
          [sg.Text('C2H2', size=(6,1), justification='l', font=font2),
           sg.Text('     '),
           sg.InputText('', key='cC2H2', size=(20,1), justification='c'),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text(''),
          #  sg.InputText('', key='rC2H2', size=(14,1), justification='c')
           ],
          [sg.Text('     ')],
          [sg.Text('C2H4', size=(6,1), justification='l', font=font2),
           sg.Text('     '),
           sg.InputText('', key='cC2H4', size=(20,1), justification='c'),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text('  '),
          #  sg.Text(''),
          #  sg.InputText('', key='rC2H4', size=(14,1), justification='c')
           ],
          [sg.Text('     ')],
          [sg.Text('     ')],
          [sg.Text('     ')],
          [sg.Text('     ')],
          [sg.Text('     ')],

          # Buttom Analisis
          [sg.Text('             '),
            sg.Button('Analisis', size=(15,1), font=font1)],
        [sg.Text('')],
    ]
#layout showing DGA Status based on the standard

layout3 = [
           #[sg.Text('     ')],
           [sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('Hasil Analisis', size=(20,1), justification='c', font=font3)],
            
            # Nama Penguji
           [sg.Text('  ')],
           [sg.Text('Nama Penguji', size=(8,2), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(20,2), key='result', background_color='lightgrey', text_color='black', justification='c')],

            # Metode & Titik Kerusakan
            [sg.Text('  ')],
           [sg.Text('Metode', size=(8,2), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(8,2), key='result', background_color='lightgrey', text_color='black', justification='c'),
            sg.Text('  '),
            sg.Text('Titik Kerusakan', size=(8,2), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(8,2), key='result', background_color='lightgrey', text_color='black', justification='c'),
            sg.Text('  ')],
           
           # Deskripsi Hasil titik kerusakan
           [sg.Text('  ')],
           [sg.Text('Deskripsi', size=(8,1), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(30,5), key='result', background_color='lightgrey', text_color='black', justification='c'),
            sg.Text('  ')],

           # Penamaan
           [sg.Text('  ')],
           [sg.Text('Sela Aulia Siswanto \nTeknik Informatika \nPoliteknik Negeri Malang \nEkojono, ST,. M.Kom. \n© 2023',size=(30,5),background_color='#4a4740', text_color='white',justification='l',font=font2)]
          ]

#layout for button
LayoutButton = [
                # Penamaan Halaman
                [sg.Text(' ')], 
                [sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('Halaman Perhitungan', size=(70,1), justification='c', font=font3)],
                
                # Button Halaman
                [sg.Text('                                              '),
                 sg.Text('                                              '),
                 sg.Text(' '),
                 sg.Button('Perhitungan', size=(10,1), font=font1),
                 sg.Button('History', size=(10,1), font=font1)],                 
               ]

#main layout
layout = [
          #[sg.Text('', size=(25,1), justification='c', font=font3),
          [sg.Text(' ')],
           [sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('Identifikasi Kegagalan Transformator Dengan DTM DPM', size=(65,1), justification='c', font=font3)],
          [sg.Text('  ')],
          [sg.Frame('', layout1, font=font1), 
           sg.Frame('', layout2, font=font2),
           sg.Frame('', layout3, font=font2)
            ], 
          LayoutButton
    ]

# Membuat Tampilan Popup Input Nama Penguji dan Nama Transformator
Layout_Popup =[
     [sg.Text('Masukkan nama penguji:')],
     [sg.Input(key='Nama_penguji')],
     [sg.Text(' ')],
     [sg.Text('Masukkan nama transformator:')],
     [sg.Input(key='Nama_transformator')],
     [sg.Text(' ')],
     [sg.Button('OK'), sg.Button('Batal')]
] 
            

#showing the window
window = sg.Window('Identifikasi Kegagalan Transformator', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED: break

    # Bagian Popup (Untuk melanjutkan ke haaman popup melalui button)
    if event == 'Input':
        # Membuat objek window dari layout popup
        popup = sg.Window('Input Nama Penguji dan Transformator').Layout(Layout_Popup)

        # Looping event handler window popup
        while True:
            event, values = popup.Read()

            if event == 'OK':
                Nama_penguji = values['Nama_penguji']
                Nama_transformator = values['Nama_transformator']
                sg.Popup(f'Nama Penguji: {Nama_penguji}\nNama Transformator: {Nama_transformator}')
                break

            if event == 'Batal' or event == sg.WIN_CLOSED:
                break

        popup.Close()

    # Bagian Perpindahan halaman dari home ke history
    # if event == 'History':
        

    if event == 'Select Data Sample':
        sampletr = values['sample']
        if sampletr == 'Transformers 1':
            window['cH2'].update('21');
            window['rH2'].update('0');
            window['cCH4'].update('39');
            window['rCH4'].update('0');
            window['cC2H2'].update('0');
            window['rC2H2'].update('0');
            window['cC2H4'].update('2');
            window['rC2H4'].update('0.401');
            window['cC2H6'].update('53');
            window['rC2H6'].update('8.699');
        
     
        if sampletr == 'Transformers 2':    #BALONGBENDO 2, STATUS 2
            window['cH2'].update('85');
            window['rH2'].update('18.639');
            window['cCH4'].update('43');
            window['rCH4'].update('6.982');
            window['cC2H2'].update('0');
            window['rC2H2'].update('0');
            window['cC2H4'].update('2');
            window['rC2H4'].update('0.472');
            window['cC2H6'].update('55');
            window['rC2H6'].update('9.592');
            
        if sampletr == 'Transformers 3':    #BAMBE 2, STATUS 3
            window['cH2'].update('33000');
            window['rH2'].update('21781.330');
            window['cCH4'].update('188000');
            window['rCH4'].update('124662.671');
            window['cC2H2'].update('0');
            window['rC2H2'].update('0');
            window['cC2H4'].update('221000');
            window['rC2H4'].update('145903.047');
            window['cC2H6'].update('132000');
            window['rC2H6'].update('87587.747');
            
            
            
    if event == 'Clear Data':
        window['cH2'].update('');
        window['rH2'].update('');
        window['cCH4'].update('');
        window['rCH4'].update('');
        window['cC2H2'].update('');
        window['rC2H2'].update('');
        window['cC2H4'].update('');
        window['rC2H4'].update('');
        window['cC2H6'].update('');
        window['rC2H6'].update('');
    
#     #DPM
#     #DPM PERCENTAGE
    
# #     if event == 'DPM 1':
         

window.close()