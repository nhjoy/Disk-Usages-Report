#!usr/bin/python3

#import library
import sys

#check if standalone program
if __name__ == "__main__":
    path ='/home'
    print ("total arguments passed: ", len(sys.argv))

    if len(sys.argv) >= 2:
        directory = sys.argv[1]
    else:
        directory = path