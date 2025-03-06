from sys import *
import os
import hashlib
import time

def Hash_File(path,blocksize = 1024):
    file = open(path,'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) >0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()

def FindDuplicate(Dir):
    flag = os.path.isabs(Dir)

    if flag == False:
        path = os.path.abspath(Dir)

    exists = os.path.isdir(path)
    dups = {}
    keys = []
    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            for filen in fileList :
                path = os.path.join(dirName,filen)
                file_hash = Hash_File(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        path = os.path.abspath(Dir)
        separator = "-" * 80
        log_path = os.path.join(path, "MarvellousLog%s.log" % time.time())
        print(log_path)
        f = open(log_path, 'w')
        f.write(separator + "\n")
        f.write("Marvellous Infosystems Process Logger : %f" % time.time() + "\n")
        f.write(separator + "\n")
        for keys, values in dups.items():
            f.write("%s\n" % values)



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
        FindDuplicate(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)


if __name__ == "__main__":
    main()