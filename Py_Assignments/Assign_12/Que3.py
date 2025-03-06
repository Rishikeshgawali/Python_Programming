import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log" %time.time())
    print(log_path)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : %f" % time.time()+"\n")
    f.write(separator + "\n")

    iterator = []

    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        iterator.append(pinfo)


    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Application name : ", argv[0])

    if (len(argv) != 2):
        print("Error : Invalid Number of Arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script is used log record of running processes")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("usage : ApplicationName AbsolutePath_Of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error : Invalid Input")


if __name__ == "__main__":
    main()
