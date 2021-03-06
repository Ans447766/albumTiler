from PIL import Image
import os
from os.path import expanduser
from pathlib import Path
def series():
    image_path = raw_input('path to image: ')
    with Image.open(image_path) as img:
        width = img.size[0]
        height = img.size[1]
    name = 1
    a = width/4
    i = height/a
    i = int(i)
    print "PROPERTIES"
    print "IMAGE WIDTH:"+str(width)+" IMAGE HEIGHT:"+str(height)+" TILE WIDTH AND HEIGHT:"+str(a)+" ROWS:"+str(i)
    x1 = 0
    y1 = 0
    x2 = y2 = a
    img_name = Path(image_path).stem
    os.mkdir(str(img_name) + "tiled")
    for x in range(i):
        for y in range(4):
            # create folder with image name
            saved_location = img_name + 'tiled/' + str(name) + '.jpg'
            coords = (x1,y1,x1+x2,y1+y2)
            imgO = Image.open(image_path)
            cropped_image = imgO.crop(coords)
            cropped_image.save(saved_location)
            x1 = x1 + int(a)
            name = name + 1
        y1 = y1 + int(a)
        x1 = 0
    print('TILLING_COMPLETED ----------------------------> ' + str(name - 1) + ' TILES EXPORTED')
series()