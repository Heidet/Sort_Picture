import os    
from PIL import Image   



def resize(self, remotepath):
    dirs = os.listdir(remotepath)
    for file in dirs:
        x = file.endswith('.png')
        print(x)
        if x == True: 
            im = Image.open(os.path.join(remotepath, file))
            size_small = im.resize((taillesmall1, taillesmall2)) #41 41 
            size_small.save(os.path.join(remotepath + r'\Petite', file), "PNG")
            size_small = im.resize((big1, big2)) #61 61 
            size_small.save(os.path.join(remotepath + r'\Grande', file), "PNG")
