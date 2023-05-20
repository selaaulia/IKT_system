import PySimpleGUI as sg

# definisi tampilan awal (home page)
home_layout = [[sg.Text("Ini adalah halaman utama.")],
               [sg.Button("Pindah ke halaman deskripsi")]]

# definisi tampilan deskripsi (description page)
desc_layout = [[sg.Text("Ini adalah halaman deskripsi.")],
               [sg.Button("Kembali ke halaman utama")]]

# buat window pertama dengan layout home_layout
window = sg.Window("Aplikasi dengan dua halaman", home_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Pindah ke halaman deskripsi":
        # tutup window pertama dan buka window kedua dengan layout desc_layout
        window.close()
        window = sg.Window("Halaman Deskripsi", desc_layout)
    if event == "Kembali ke halaman utama":
        # tutup window kedua dan buka window pertama dengan layout home_layout
        window.close()
        window = sg.Window("Aplikasi dengan dua halaman", home_layout)

window.close()
