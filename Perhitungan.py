# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import math
import numpy as np
import io
from PIL import Image

#create theme
sg.theme('DarkTeal11')

#font
font1 = ("Arial", 12, 'bold')
font2 = ("Arial", 12)
font3 = ("Arial", 16, 'bold')

# sg.set_options(font=font1)
sg.SetOptions(element_padding=((1,1),0))

#layout left
layout1 = [
            # Judul Input Data Kandungan Konsentrasi Gas
            [sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('Inputan Konsentrasi Gas', size=(20,1), justification='c', font=font3)],

          [sg.Text('')],
          [sg.Text('Gas', size=(5,1), justification='l', font=font1),
           sg.Text('Concentration (ppm)', size=(17,1), justification='l', font=font1),
           sg.Text('Rate (ppm/year)',size=(15,1), justification='l', font=font1)],
          [sg.Text('')],
          
          [sg.Text('H2', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cH2', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rH2', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('CH4', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cCH4', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rCH4', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('C2H2', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cC2H2', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rC2H2', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('C2H4', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cC2H4', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rC2H4', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('C2H6', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cC2H6', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rC2H6', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('  ')],

          # Buttom Analisis
          [sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
            sg.Button('Analisis', size=(15,1), font=font1)],
        [sg.Text('')],
    ]
#layout showing DGA Status based on the standard

layout2 = [
           #[sg.Text('     ')],
           [sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('  '),
            sg.Text('Hasil Analisis', size=(15,1), justification='c', font=font3)],
            
            # Metode yang digunakan DTM/DPM
           [sg.Text('  ')],
           [sg.Text('Metode', size=(8,2), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(8,2), key='result', background_color='lightgrey', text_color='black', justification='c')],

            #Titik Kerusakan
            [sg.Text('  ')],
           [sg.Text('Titik Kerusakan', size=(8,2), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(8,2), key='result', background_color='lightgrey', text_color='black', justification='c')],
           
           # Deskripsi Hasil titik kerusakan
           [sg.Text('  ')],
           [sg.Text('Deskripsi', size=(8,1), justification='c', font=font2),
            sg.Text('  '),
            sg.Text('',size=(30,5), key='result', background_color='lightgrey', text_color='black', justification='c')],

           # Penamaan
           [sg.Text('  ')],
           [sg.Text('Sela Aulia Siswanto \nTeknik Informatika \nPoliteknik Negeri Malang \nEkojono, ST,. M.Kom. \n© 2023',size=(30,5),background_color='#4a4740', text_color='white',justification='l',font=font2)]
          ]

# # Pengidentifikasian gambar yang ditampilkan
#     # membuka gambar dengan PIL
# image = Image.open("DTM.png")
# # image2 = Image.open("DPM.png")

# # mengubah ukuran gambar menjadi 300x300 pixel
# image = image.resize((350, 150))

# # mengubah gambar menjadi objek byte
# bio = io.BytesIO()
# image.save(bio, format="PNG")
# # image2.save(bio, format="PNG")
# image_bytes = bio.getvalue()

# #layout gambar DTM dan DPM
# layout3 = [ # Label Judul Layout
#             [sg.Text('GAMBAR POSISI DTM & DPM', size=(33,1), justification='c', font=font1)],
#             [sg.Text('  ')],

#             # Label DTM
#             [sg.Text('Duval Triangle Method (DTM)', size=(23,1), justification='c', font=font1),],
#             [sg.Text(' ')],
#             # Menampilkan Gambar DTM
#             [sg.Image(data=image_bytes)],
#             [sg.Text(' ')],

#             # Label DPM
#             [sg.Text('Duval Pentagon Method (DPM)', size=(24,1), justification='c', font=font1),]
#             # Menampilkan Gambar DPM
#             # [sg.Image(data=image_bytes)]
#         ]


#layout for button
LayoutButton = [
                # Label nama penguji dan nama transformator
                [sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('Nama Penguji', size=(20,1), justification='l', font=font1),
                 sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('        '),
                 sg.Text('Nama Transformator', size=(17,1), justification='l', font=font1)],
                 
                 # Input nama penguji
                [sg.Text('Nama Penguji', size=(12,1), justification='l', font=font2),
                    sg.InputText('', key='cC2H6', size=(25,1), justification='c'),
                    sg.Button('Submit', size=(8,1), font=font1),
                
                # Pilih Transformator yang diuji
                 sg.Text('  '),
                 sg.Button('Pilih Transformator', size=(11,2), font=font1),
                 sg.Combo(values=('Transformers 1','Transformers 2', 'Transformers 3'), size=(17, 1), key='sample'),
                 sg.Button('Hapus', size=(8,1), font=font1)],

                # Penamaan Halaman
                [sg.Text(' ')], 
                [sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('Halaman Perhitungan', size=(20,1), justification='c', font=font3)],
                
                # Button Halaman
                [sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
                 sg.Text('    '),
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
            sg.Text('Identifikasi Kegagalan Transformator Dengan DTM DPM', size=(45,1), justification='c', font=font3)],
          [sg.Text('  ')],
          [sg.Frame('', layout1, font=font1), 
           sg.Frame('', layout2, font=font2)
        #    sg.Frame('', layout3, font=font2)
            ], 
          LayoutButton
    ]

#showing the window
window = sg.Window('Identifikasi Kegagalan Transformator', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED: break

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