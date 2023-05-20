import io
import PySimpleGUI as sg
from PIL import Image

# membuka gambar dengan PIL
image = Image.open("DPM.png")

# mengubah gambar menjadi objek byte
bio = io.BytesIO()
image.save(bio, format="PNG")
image_bytes = bio.getvalue()

# membuat layout dengan komponen Image
layout = [[sg.Image(data=image_bytes)]]

# membuat jendela aplikasi dengan layout
window = sg.Window("Contoh Menampilkan Gambar dalam Layout dengan Python dan SimpleGUI", layout)

# menjalankan loop utama SimpleGUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# menutup jendela aplikasi saat loop selesai
window.close()
