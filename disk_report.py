#!usr/bin/python3

#import library
import sys
import os
import pandas as pd

#function- calculate disk space by each dir
def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
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
    
    #list created
    usage = []
    paths = []

    #loop to access sub-directories and files
    for entry in os.scandir(directory):
        print(entry.path)
        #checks entry is directory and make sure not symbolic link
        if (entry.is_dir(follow_symlinks=False)):
            # print(entry.path + " is a directory")
            # print(get_size(entry.path))
            
            #appending the value of total and path in the lists
            total = get_size(entry.path)
            print(total)
            paths.append(entry.path)
            usage.append(total)
        
        #dictionary created
        usage_dict = {'directory' : paths, 'usage' : usage}
        df = pd.DataFrame(usage_dict)
        print(df)
        df.to_csv("disk_usages.csv")