import cv2
from pyzbar.pyzbar import decode

class EmptyList(Exception):
    def __init__(self, message = "Error al leer el código QR"):
        self.message = message
        super().__init__(self.message)

class QrReader:
    def __init__(self,qr_name):
        self.qr_name = qr_name

    def read(self):
        image_reader = cv2.imread(self.qr_name)
        qr_decode = decode(image_reader)
        if len(qr_decode) == 0:
            raise EmptyList()
        else:
            for code in qr_decode:
                qr_information = code.data.decode('utf-8')
                print(qr_information)
    


# def qr_reader(image):
#     image_reader = cv2.imread(image)
#     qr_decode = decode(image_reader)
#     if len(qr_decode) == 0:
#         print('Error al leer el código QR')
#     else:
#         for code in qr_decode:
#             qr_information = code.data.decode('utf-8')
#             print(qr_information)

# img1 = 'test_pil_0.png'

# qr_reader(img1)

