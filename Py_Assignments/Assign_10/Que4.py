import os
import shutil
from sys import *

def Directory_Copy(From_Dir,Ext1,To_Dir):
    flag = os.path.isabs(From_Dir)
    if flag == False:
        path = os.path.abspath(From_Dir)

    if not os.path.isdir(To_Dir):
        os.makedirs(To_Dir)

    flag = os.path.isabs(To_Dir)
    if flag == False:
        path1 = os.path.abspath(To_Dir)

    for Foldername,subfolder,filename in os.walk(path):
        print("Folder name is : ",Foldername)
        for fname in filename:
            if fname.endswith(Ext1):
                new_name = os.path.join(Foldername,fname)
                shutil.copy(new_name,path1)
                print(new_name)


def main():

    print("Application name : ", argv[0])

    if (len(argv) != 4):
        print("Error : Invalid Number of Arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used log record of running processes")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("usage : ApplicationName Directory1 .extension Directory2")
        print("Directory1 = Copy files from this directory ,.extension = copy only those files having .extension")
        print("Directory2 = Copy files to this directory")
        exit()

    Directory_Copy(argv[1],argv[2],argv[3])


if __name__ == "__main__":
    main()


