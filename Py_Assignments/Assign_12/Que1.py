import psutil

def ProcessIterator():

    iterator = []

    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs = ['pid' , 'name' , 'username'])
        iterator.append(pinfo)

    return iterator

def main():
    print("This is Application of Process Iterator...")

    List_Proc = ProcessIterator()
    for element in List_Proc:
        print(element)

if __name__ == "__main__":
    main()