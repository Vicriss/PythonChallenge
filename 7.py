# -*- encoding:utf-8 -*-

from PIL import Image
import re
x_begin, x_end = 0, 609
y_begin, y_end = 43, 52
step = 7
im = Image.open('oxygen.png')
pixel = [chr(im.getpixel((x, 43))[2]) for x in range(x_begin, x_end, step)]
msg = ''.join(pixel)
print(msg)
msg = ''.join([chr(int(c)) for c in re.findall(r'(\d{3})', msg)])
print('msg:',msg)
