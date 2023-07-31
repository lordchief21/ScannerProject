from __future__ import print_function
import sane


        

sane.init()
devices = sane.get_devices(localOnly=False)
print(devices)

dev = sane.open(devices[0][0])

#Set Params 
params = dev.get_parameters()



try:
    dev.br_x = 53
    dev.br_y = 73
    dev.tl_x = 27
    dev.tl_y = 50
    dev.resolution = 144
    dev.page_width = 203.
    dev.page_height = 95.
    dev.emphasis = 65
    # dev.contrast = 60
    dev.df_action = "Continue"
    dev.df_length = 1
except:
    print('Problems during setting params ')

params = dev.get_parameters()

opt = dev.__getattr__('optlist')

print(params)

width = dev.page_width
height = dev.page_height
b5 = dev.contrast
test_option = dev.df_length
print(opt)
print(width)
print(height)
print("resolution",b5)
print("Test",test_option)

i = 0
while dev.multi_scan():
    dev.start()
    im = dev.snap()
    im.save('test_pil_'+'err2'+'.png')
    print(width,height)
    i +=  1
