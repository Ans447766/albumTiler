def series():
    from PIL import Image
    import os
    from os.path import expanduser
    image_path = '2096.jpg'
    image_obj = Image.open(image_path)
    image_name = os.path.basename(image_path)
    # getting image height and width
    with Image.open(image_path) as img:
        width = img.size[0]
        height = img.size[1]
    name = 0
    a = width/4
    i = height/a
    print "width:"+str(width)+" height:"+str(height)+" a:"+str(a)+" i:"+str(i)
    x1 = 0
    y1 = 0
    x2 = a
    y2 = a
    print "x1:"+str(x1)+" y1:"+str(y1)+" x2:"+str(x2)+" y2:"+str(y2)
    for x in range(2):
        for x in range(4):
            print "x1:"+str(x1)+" y1:"+str(y1)+" x2:"+str(x2)+" y2:"+str(y2)
            saved_location = str(name) + '.jpg'
            cropped_image = image_obj.crop(x1,y1,x2,y2)
            cropped_image.save(saved_location)
            x1 = x1 + int(a)
            print "name:" + str(name)
            name = name + 1
        y1 = y1 + int(a)
        x1 = 0

series()