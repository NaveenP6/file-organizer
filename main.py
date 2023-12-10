# Naveen Prabaharan
# 12/10/23

# Whenever I download an image, it won't go to the regular downloads folder, 
# instead this python script will organize the files into different subfolders for easier access to them later. 
# It will run in the background on my computer.

import os

path = "C:\\Users\\nphn6\\Downloads" #Always run this program within the home directory of your computer
obj = os.scandir(path)
 
# List all files and directories 
# in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj :
    if entry.is_dir() or entry.is_file():
        print(entry.name)
 
 
# entry.is_file() will check
# if entry is a file or not and
# entry.is_dir() method will
# check if entry is a
# directory or not. 
 
 
# To Close the iterator and
# free acquired resources
# use scandir.close() method
obj.close()

