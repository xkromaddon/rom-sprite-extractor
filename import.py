import os
import sys
import re

from PIL import Image
from PIL import ImageFilter

name = ""
x = 0
y = 0
w = 0
h = 0
pt = 0
pb = 0
pl = 0
pr = 0

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

texture = os.listdir("Texture2D")
files = os.listdir("MonoBehaviour")
for i in range(len(files)):
    print(files[i], texture[i])
    filepath = "MonoBehaviour/" + files[i]
    imagepath = "Texture2D/" + texture[i]
    savepath = "finish"
    
    #try to open file
    try:
        fh = open(filepath, encoding="utf8")
        im = Image.open(imagepath)
    except:
        continue
    
    for line in fh:
        str_line = line.strip()
        name_re = re.search(r"string name = \"(.*)\"", str_line)
        x_re = re.search(r"int x = (.*)", str_line)
        y_re = re.search(r"int y = (.*)", str_line)
        w_re = re.search(r"int width = (.*)", str_line)
        h_re = re.search(r"int height = (.*)", str_line)
        pl_re = re.search(r"int paddingLeft = (.*)", str_line)
        pr_re = re.search(r"int paddingRight = (.*)", str_line)
        pt_re = re.search(r"int paddingTop = (.*)", str_line)
        pb_re = re.search(r"int paddingBottom = (.*)", str_line)
        
        if name_re:
            name = name_re.group(1)
            
        if x_re:
            x = int(x_re.group(1))

        if y_re:
            y = int(y_re.group(1))

        if w_re:
            w = int(w_re.group(1))

        if h_re:
            h = int(h_re.group(1))

        if pl_re:
            pl = int(pl_re.group(1))

        if pr_re:
            pr = int(pr_re.group(1))

        if pt_re:
            pt = int(pt_re.group(1))
            
        if pb_re:
            pb = int(pb_re.group(1))
            crop_rec = (x, y, x + w, y + h)
            im_cropped = im.crop(crop_rec)
            im_final = add_margin(im_cropped, pt, pr, pb, pl, (0,0,0,0))
            im_final.save(savepath + "/" + name + ".png", "png")
            
    fh.close()