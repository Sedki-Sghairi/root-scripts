#!/usr/bin/env python3
import os
from PIL import Image
import glob

dest_dir = '/home/kali/opt/icons/'
images = glob.glob('./images/*.webp')
for i in images:

   im = Image.open(i)
   new_im = im.rotate(90).resize((128,128))
   root, ext = os.path.splitext(i)
   name = i[9:]
   new_im.save(dest_dir + name,'JPEG')