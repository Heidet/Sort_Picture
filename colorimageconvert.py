from PIL import Image
from PIL import ImageColor
import glob, os
import shutil, os 

class Sort_picture:
    def __init__(self):
        self.rootpath = r"C:\Users\Antoine Heidet\Desktop\Mes projets\ProjetTrieIcon\icon\serie2"
        self.blue = (12, 112, 143),(12, 112, 144),(13, 113, 145),(30, 147, 207),(30, 147, 208),(33, 96, 171),(47, 162, 219),(41, 64, 145),(41, 64, 146),(33, 96, 170),(13, 113, 146),(47, 162, 220),(6, 96, 124),(48, 164, 220),(6, 96, 123)
        self.yellow = (254, 211, 21),(254, 213, 21)
        self.red = (184, 23, 32),(191, 19, 62),(190, 19, 61),(153, 33, 32),(191, 19, 63),(213, 11, 80),(190, 19, 62),(195, 17, 65)
        self.orange = (238, 112, 13),(236, 96, 20),(243, 143, 1),(243, 145, 0)
        self.green = (112, 165, 42),(0, 114, 54),(112, 165, 43),(0, 130, 59),(112, 165, 43),(115, 167, 42),(0, 145, 63),(115, 167, 42),(146, 191, 31),(130, 179, 37),(115, 167, 41),(130, 179, 36),(0, 141, 61)
        self.purple = (149, 27, 129)

    def detect(self,rootpath):
        data = []
        listimg = os.listdir(rootpath)
        for img in listimg:
            i = Image.open(os.path.join(rootpath, img))
            i = i.convert("RGB")
            image = Image.Image.getcolors(i)
            data.append(image[1][1])
        return data, listimg


    def check_color(self,rootpath,rgb_img,targetpath):
        data, listimg = self.detect(rootpath)
        for i, rgb in enumerate(data):
            print(rgb)
            if rgb == rgb_img:
                if os.path.exists(targetpath):
                    print('image déplacer')
                    shutil.move(os.path.join(rootpath, listimg[i]), targetpath)

    def move_targetpath(self):
        if self.blue:
            for i in self.blue:
                self.check_color(self.rootpath, i, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\bleu")
        if self.green:
            for i in self.green:
                self.check_color(self.rootpath, i, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\vert")
        if self.yellow:
            for i in self.yellow:
                self.check_color(self.rootpath, i, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\jaune")
        if self.red:
            for i in self.red: 
                self.check_color(self.rootpath, i, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\rouge")
        if self.orange:
            for i in self.orange: 
                self.check_color(self.rootpath, i, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\orange")
        if self.purple:
            self.check_color(self.rootpath, self.purple, r"C:\Users\Antoine Heidet\Desktop\icon\Serie\Serie2\violet")


sort_picture = Sort_picture()
sort_picture.move_targetpath()
