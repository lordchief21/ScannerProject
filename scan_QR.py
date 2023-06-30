import cv2
from pyzbar.pyzbar import decode

def qr_reader(image):
    image_reader = cv2.imread(image)
    qr_decode = decode(image_reader)
    if len(qr_decode) == 0:
        print('Error al leer el código QR')
    else:
        for code in qr_decode:
            qr_information = code.data.decode('utf-8')
            print(qr_information)

img1 = 'test_pil_0.png'

qr_reader(img1)