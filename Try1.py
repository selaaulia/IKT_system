import PySimpleGUI as sg
import layout1
import layout2_a
import layout2_b

# Buat window dengan layout awal (Halaman 1)
window = sg.Window('Multi-Layout', layout1.create_layout1())

current_layout = 'layout1'  # Layout saat ini

# Loop untuk membaca event dari window
while True:
    event, _ = window.read()

    # Jika tombol "Pindah ke Halaman 2" ditekan
    if event == 'Pindah ke Halaman 2':
        window.close()  # Tutup window saat ini
        window = sg.Window('Multi-Layout', layout2_a.create_layout2_a())  # Buka window baru dengan layout Halaman 2 - Tampilan A
        current_layout = 'layout2_a'

    # Jika tombol "Tampilkan Tampilan B" ditekan (pada Halaman 2 - Tampilan A)
    elif event == 'Tampilkan Tampilan B' and current_layout == 'layout2_a':
        window.close()  # Tutup window saat ini
        window = sg.Window('Multi-Layout', layout2_b.create_layout2_b())  # Buka window baru dengan layout Halaman 2 - Tampilan B
        current_layout = 'layout2_b'

    # Jika tombol "Tampilkan Tampilan A" ditekan (pada Halaman 2 - Tampilan B)
    elif event == 'Tampilkan Tampilan A' and current_layout == 'layout2_b':
        window.close()  # Tutup window saat ini
        window = sg.Window('Multi-Layout', layout2_a.create_layout2_a())  # Buka window baru dengan layout Halaman 2 - Tampilan A
        current_layout = 'layout2_a'

    # Jika tombol "Exit" ditekan atau window ditutup, keluar dari loop
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

# Tutup window terakhir
window.close()
