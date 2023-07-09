import qrcode as qc

from PIL import Image

qr = qc.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
qr.add_data("https://chat.openai.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="red")
img.save("wert.png")