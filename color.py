#!/usr/bin/python

# http://stackoverflow.com/questions/1616767/pil-best-way-to-replace-color

from PIL import Image
import sys

img = Image.open(sys.argv[1])
img = img.convert("RGBA")

pixdata = img.load()

# Clean the background noise, if color != white, then set to black.
# change with your color
for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y][0] < 20:
            pixdata[x, y] = (255, 0, 0, 255)

img.save("tt.png")            


