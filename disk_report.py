#!usr/bin/python3

#import library
import sys
import os

#function- calculate disk space by each dir
def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else Exception as e:
                print("Exception: ", e)
                total += 0
    return total
    

#check if standalone program
if __name__ == "__main__":
    path ='/home'
    print ("total arguments passed: ", len(sys.argv))

    if len(sys.argv) >= 2:
        directory = sys.argv[1]
    else:
        directory = path

    #loop to access sub-directories and files
    for entry in os.scandir(directory):
        print(entry.path)
        #checks entry is directory and make sure not symbolic link
        if (entry.is_dir(follow_symlinks=False)):
            print(entry.path + " is a directory")
            ptint(get_size(entry.path))