# import os



# files = [ f for f in os.listdir(rootpath) if f[-4:].lower() in (".jpg",".png") ] # Pour chaques files si les 4 dernier caractère son .png ou .jpg


# for index, filename in enumerate(files):
#     extension = os.path.splitext(filename)[1]
#     # print(extension)
#     newname = "picture-%05d%s" % (index,extension)
#     if os.path.exists(newname):
#         print("Cannot rename %s to %s, already exists" % (filename,newname))              
#     else:
#         print("Renaming %s to %s" % (filename,newname))
#         # os.rename(r'C:\Users\Antoine Heidet\Desktop\Mes projets\ProjetTrieIcon\icon\{filename}', r'C:\Users\Antoine Heidet\Desktop\Mes projets\ProjetTrieIcon\icon\{newname}')
#         os.rename(os.path.join(rootpath, filename), os.path.join(rootpath, newname))

