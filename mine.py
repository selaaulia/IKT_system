# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:42:14 2023

@author: 16agn
"""

import PySimpleGUI as sg
import math
import numpy as np

#create theme
sg.theme('DarkGray9')

#font
font1 = ("Arial", 12, 'bold')
font2 = ("Arial", 12)
font3 = ("Arial", 16, 'bold')

# sg.set_options(font=font1)
sg.SetOptions(element_padding=((1,1),0))

#layout left
layout1 = [
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
          [sg.Text('CO', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cCO', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rCO', size=(14,1), justification='c')],
          [sg.Text('     ')],
          [sg.Text('CO2', size=(6,1), justification='l', font=font2),
           sg.InputText('', key='cCO2', size=(17,1), justification='c'),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text('  '),
           sg.Text(''),
           sg.InputText('', key='rCO2', size=(14,1), justification='c')],
          [sg.Text('')],
          [sg.Text('')],
          [sg.Text('')],
    ]
#layout showing DGA Status based on the standard

layout2 = [
           #[sg.Text('     ')],
           [sg.Text('DGA STATUS', size=(33,1), justification='c', font=font1)],
           [sg.Text('  ')],
           [sg.Text('Standard', size=(10,1), justification='c', font=font2),
            sg.Radio('IEC', "RADIO1", key='IEC', default=True),
            sg.Radio('IEEE', "RADIO1", key='IEEE')],
           [sg.Text('  ')],
           [sg.Text('Result', size=(8,2), justification='c', font=font2),
            sg.Text(size=(25,2), key='result', background_color='lightgrey', text_color='black', justification='c')],
           [sg.Text(' ')],
           #button
           [sg.Button('ANALYZE', size=(20,1), font=font1),
            sg.Button('CLEAR', size=(10,1), font=font1)],
           #[sg.Text('')],
           [sg.Text('_'*40)],
           
           
           #fault identification
           [sg.Text('FAULT IDENTIFICATION', size=(33,1), justification='c', font=font1)],
           [sg.Text('  ')],
           [sg.Text('Method', size=(8,1), justification='c', font=font2),
            sg.Combo(values=[#'DRM', 'RRM', 'IRM', 
                             'DTM 1', 'DTM 4', 'DTM 4', 
                             'DPM 1', 'DPM 2'], key='mm')],
           [sg.Text(' ')],
           [sg.Text('Resul', size=(8,1), justification='c', font=font2),
            sg.Text(size=(25,3), key='result', background_color='lightgrey', text_color='black', justification='c')],
           [sg.Text(' ')],
           #button
           [sg.Button('ANALYZE', size=(20,1), font=font1),
            sg.Button('CLEAR', size=(10,1), font=font1)],
           [sg.Text(' ')],
          ]

#layout recommended action
layout3 = [
            [sg.Text('RECOMMENDED ACTION', size=(33,1), justification='c', font=font1)],
            [sg.Text('  ')],
            [sg.Text('Result', size=(8,1), justification='c', font=font2),
             sg.Text(size=(22,12), key='result', background_color='lightgrey', text_color='black', justification='c')],
            [sg.Text(' ')],
            [sg.Text(' ')],
            [sg.Text(' ')],
            [sg.Text(' ')],
            [sg.Text('Julia Agnes Furqonil Iman \nElectrical System Engineering \nPoliteknik Negeri Malang \nDr. Rahman Azis Prasojo, SST., MT. \n© 2023',size=(30,5),background_color='#4a4740', text_color='white',justification='l',font=font2)]

            
    ]


#layout for button
LayoutButton = [
                [sg.Text(' ')],
                [sg.Button('Select Data Sample', size=(17,1), font=font1),
                 sg.Combo(values=('Transformers 1','Transformers 2', 'Transformers 3'), size=(15, 1), key='sample'),
                 sg.Button('Clear Data', size=(12,1), font=font1)],
                [sg.Text(' ')],
               ]

#main layout
layout = [
          [sg.Text('', size=(25,1), justification='c', font=font3),
           sg.Text('Multi Method Transformers Fault Analysis', size=(35,1), justification='c', font=font3)],
          [sg.Text('  ')],
          [sg.Frame('', layout1, font=font1), 
           sg.Frame('', layout2, font=font2), 
           sg.Frame('', layout3, font=font2)], 
          LayoutButton
    ]

#showing the window
window = sg.Window('DGA MULTI METHOD', layout)
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
            window['cCO'].update('226');
            window['rCO'].update('23.775');
            window['cCO2'].update('2783');
            window['rCO2'].update('570.422');
     
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
            window['cCO'].update('217');
            window['rCO'].update('16.606');
            window['cCO2'].update('1326');
            window['rCO2'].update('172.955');
            
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
            window['cCO'].update('315000');
            window['rCO'].update('210290.489');
            window['cCO2'].update('2236000');
            window['rCO2'].update('1492309.936');
            
            
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
        window['cCO'].update('');
        window['rCO'].update('');
        window['cCO2'].update('');
        window['rCO2'].update('');
    
#     #DPM
#     #DPM PERCENTAGE
    
# #     if event == 'DPM 1':
         

window.close()
    



