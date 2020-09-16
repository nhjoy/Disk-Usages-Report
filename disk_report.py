#!usr/bin/python3

#import library
import sys
import os

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
