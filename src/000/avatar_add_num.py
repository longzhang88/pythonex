#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://github.com/Show-Me-the-Code/show-me-the-code
No.000
read a picture and add number at the top right
"""
import sys
from PIL import Image, ImageDraw, ImageFont

original_avatar = 'weChat_avatar.png'   # input picture
saved_avatar = 'new_avatar.png' # output picture
windows_font = 'arial.ttf'  # windows font arial
color = (255, 0, 0) # text color: red

def draw_text(text, fill_color, windows_font):
    try:
        im = Image.open(original_avatar)
        x, y =  im.size
        print "The size of the Image is: "
        print(im.format, im.size, im.mode)
        im.show()
        
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(windows_font, 35)
        draw.text((x-20, 7), text, fill_color, font)
        
        im.save(saved_avatar)
        im.show()

    except:
        print "Unable to load image"

if __name__ == "__main__":
    #number = str(raw_input('please input number: '))
    number = sys.argv[1]
    draw_text(number, color, windows_font)



