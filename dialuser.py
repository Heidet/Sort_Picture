import os
from conf.colorimageconvert import Sort_picture
# r"C:\Users\Antoine Heidet\Desktop\Mes projets\ProjetTrieIcon\icon"
# r"C:\Users\Antoine Heidet\Desktop\icon"

def user_conf():
    print('Welcome')
    print('Please enter the hostname for SFTP :')
    rootpath = input()
    print('Please enter the username :')
    remotepath = input()
    return rootpath, remotepath


rootpath, remotepath = user_conf()
main = Sort_picture(rootpath, remotepath)
main.move_targetpath()
