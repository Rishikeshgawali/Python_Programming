

import os

def File_Check(F_Name):
    if(os.path.exists(F_Name)):
        print("File Exists...")
        fd = open(F_Name,'r')
        Data = fd.read()
        print(Data)
        
    else:
        print("File not exist")

def main():
    print("Enter the name of file : ")
    File_Name = input()
    File_Check(File_Name)


if __name__ == "__main__":
    main()