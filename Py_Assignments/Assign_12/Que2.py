from sys import *
import os
import psutil

def ProcessIterator(process):

    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs = ['pid' , 'name' , 'username'])
        if process == pinfo['name']:
             break

    return pinfo

def main():
    print("This is Application of Process Iterator...")

    List_Proc = ProcessIterator(argv[1])
    print(List_Proc)

if __name__ == "__main__":
    main()