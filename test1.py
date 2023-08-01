
import sane


        

sane.init()
devices = sane.get_devices(localOnly=False)
print(devices)

dev = sane.open(devices[0][0])
dev2 = sane.open(devices[1][0])
#Set Params 
params = dev.get_parameters()
params2 = dev2.get_parameters()


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

    dev2.br_x = 53
    dev2.br_y = 73
    dev2.tl_x = 27
    dev2.tl_y = 50
    dev2.resolution = 144
    dev2.page_width = 203.
    dev2.page_height = 95.
    dev2.emphasis = 65
    # dev.contrast = 60
    dev2.df_action = "Continue"
    dev2.df_length = 1
except:
    print('Problems during setting params ')

params = dev.get_parameters()
params2 = dev2.get_parameters()

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
while dev.multi_scan() or dev2.multi_scan():
    dev.start()
    dev2.start()
    im = dev.snap()
    im2 = dev2.snap()
    im.save('test_pil_'+'err2'+'.png')
    im2.save('test_pil_'+'err3'+'.png')
    print(width,height)
    i +=  1
