from __future__ import print_function
import sane
from scan_QR import QrReader

def devices():
    sane.init()
    device = sane.get_devices()
    dev = sane.open(device[0][0])

    return dev


class Scanner:

    def __init__(self, device = devices()) -> None:
        self.device = device

    def confg_scanner(self, br_x = 60,br_y = 73,tl_x = 27,tl_y = 50,resolution = 144,page_width = 203.00,page_height = 95.00,emphasis = 10, df_action = "Continue",df_length = 1):
        
        self.device.get_parameters()
        try:
            self.device.br_x =  br_x
            self.device.br_y = br_y
            self.device.tl_x = tl_x
            self.device.tl_y = tl_y
            self.device.resolution = resolution
            self.device.page_widht = page_width
            self.device.page_height = page_height
            self.device.emphasis = emphasis
            self.device.df_action = df_action
            self.device.df_length = df_length
        except:
            print('Problems during setting params ')
        self.device.get_parameters()

    def start_scanning(self):
        i = 0
        dev = self.device
        
        def scanning():
            dev.start()
            im = dev.snap()
            route = 'test_pil_'+str(i)+'.png'
            im.save(route)
            qr_reader = QrReader(route)
            qr_reader.read()
        
        while dev.multi_scan():
            try:
               scanning()
               i += 1
            except Exception as err:
                print(err)
                dev.cancel()
                choice = input("Desea continuar?")
                if choice == "yes":
                    scanning()
                    i += 1
                else: break
            finally:
                print("proceso finalizado")