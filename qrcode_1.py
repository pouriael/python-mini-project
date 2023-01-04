import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,border=4)
url = input("enter your url")
qr.add_data(url)
qr.make(fit = True)
img = qr.make_image(fill_color ="black",back_color="white")
image_name = input("enter your image name")
img.save(image_name +".png")
