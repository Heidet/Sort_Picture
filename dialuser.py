import os
import random
from conf.colorimageconvert import Sort_picture
from colorama import init
init() # Color window

# r"C:\Users\Antoine Heidet\Desktop\Mes projets\ProjetTrieIcon\icon"
# r"C:\Users\Antoine Heidet\Desktop\icon"

def user_conf():
    color = '\033[32m'
    print('Welcome')
    print(color + 'Please enter the folder containing the images :' '\033[0m')
    rootpath = input()
    print(color + 'Please enter the target folder : ' + '\033[0m')
    remotepath = input()
    return rootpath, remotepath

def method():
    color = '\033[32m'
    print(color + 'What do you want to do' + '\033[0m')
    print('1: Sort Images Colors')
    print('2: rezise Images')
    print('3: Rename full files')
    choice = int(input())
    return choice 

def run():
    if choice == 1: 
        main.move_targetpath()
    elif choice == 2:    
        # print('Please enter height pixel')
        # sm1 = int(input())
        # print('Please enter width pixel')
        # sm2 = int(input())
        main.resize(remotepath)
        filelist = os.listdir(remotepath)
        for i in filelist:
            filePath = remotepath + "/" + i
            if os.path.isfile(filePath):
                os.remove(filePath)
    elif choice == 3: 
        main.rename(rootpath)

rootpath, remotepath = user_conf()
main = Sort_picture(rootpath, remotepath)
choice = method()
run()
        
# rootpath, remotepath = user_conf()

# # method = method()
# choice()
# rootpath, remotepath = user_conf()
# main = Sort_picture(rootpath, remotepath)
# choice = method()
# rootpath, remotepath = user_conf()
# main = Sort_picture(rootpath, remotepath)
# choice = method()
# method()
# rootpath, remotepath = user_conf()
# main = Sort_picture(rootpath, remotepath)
# main.move_targetpath()
