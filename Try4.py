import PySimpleGUI as sg

# Data untuk tabel
data = [
    ['John', '20', 'Jl. ABC'],
    ['Jane', '25', 'Jl. DEF'],
    ['Bob', '30', 'Jl. GHI'],
    ['Alice', '35', 'Jl. JKL'],
    ['Mark', '40', 'Jl. MNO']
]

# Layout tabel
table_layout = [
    [sg.Table(values=data, headings=['Nama', 'Usia', 'Alamat'], num_rows=5, col_widths=[15, 5, 20])]
]

# Layout tambahan
additional_layout = [
    [sg.Text('Ini adalah layout tambahan')]
]

# Layout utama
layout = [
    [sg.Column(table_layout)],
    [sg.Column(additional_layout)]
]

# Membuat window
window = sg.Window('Tampilan Tabel Desktop di Beberapa Layout', layout)

# Loop event
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# Menghapus window
window.close()
