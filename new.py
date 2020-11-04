from PIL import Image
from PIL import Image
from PIL import ImageColor
import glob, os
import shutil, os 

i = Image.open("1.png")
i = i.convert("RGB")
image = Image.Image.getcolors(i)
print(image)
