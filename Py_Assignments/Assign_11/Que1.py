from sys import *
import os
import hashlib


def Hash_File(path,blocksize = 1024):
    file = open(path,'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) >0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()


def DisplayChecksum(Dir):
    flag = os.path.isabs(Dir)
    if flag == False:
        path = os.path.abspath(Dir)
    exists = os.path.isdir(path)

    if exists:
        for Dirname,subfolder,filename in os.walk(path):
            print("Folder name is : ",Dirname)
            for fname in filename:
                path = os.path.join(Dirname,fname)
                hasher = Hash_File(path)
                print(path,hasher)
    else:
        print("Invalid Path")


def main():
    print("Marvellous Infosystem by Piyush Khairnar...")

    print("Application name is : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of Arguments")

    if(argv[1] == '-h' or argv[1] == '-H'):
        print("This Script is used to traverse specific directory and display checksum of files.")

    if(argv[1] == '-u' or argv[1] == '-U'):
        print("usage : ApplictionName AbsolutePath_Of_Directory ")

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)


if __name__ == "__main__":
    main()