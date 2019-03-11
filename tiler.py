from PIL import Image
import os
from os.path import expanduser
def series():
    # image_name = os.path.basename(image_path)
    # getting image height and width
    image_path = 'sample.jpg'
    with Image.open(image_path) as img:
        width = img.size[0]
        height = img.size[1]
    name = 0
    a = width/4
    i = height/a
    i = int(i)
    print "width:"+str(width)+" height:"+str(height)+" a:"+str(a)+" i:"+str(i)
    x1 = 0
    y1 = 0
    x2 = y2 = a
    for x in range(i):
        for y in range(4):
            saved_location = "results/" + str(name) + '.jpg'
            coords = (x1,y1,x2,y2)
            image_path = 'sample.jpg'
            imgO = Image.open(image_path)
            cropped_image = imgO.crop(coords)
            cropped_image.save(saved_location)
            print "name:" + str(name) + "x1:"+str(x1)+" y1:"+str(y1)+" x2:"+str(x2)+" y2:"+str(y2) + " -- OK"
            x1 = x1 + int(a)
            name = name + 1
        y1 = y1 + int(a)
        x1 = 0

series()