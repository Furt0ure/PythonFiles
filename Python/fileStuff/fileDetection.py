import os

#path = "C:\\Users\\colin\\Downloads\\mapp"
path = "C:\\Users\\colin\\Downloads\\IMG_1956.jpg"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")