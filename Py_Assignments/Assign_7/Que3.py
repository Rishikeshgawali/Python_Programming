import time
import threading

def EvenList(Arr):
    i = 0
    Sum = 0
    for i in range(0,len(Arr)):
        if(Arr[i] % 2 == 0):
            Sum = Sum + Arr[i]
            print("Even number is : ",Arr[i])
    print("Sum of Even Number is : ",Sum)


def OddList(Arr):
    i = 0
    Sum = 0
    for i in range(0,len(Arr)):
        if(Arr[i] % 2 != 0):
            Sum = Sum + Arr[i]
            print("Odd number is : ", Arr[i])
    print("Sum of Odd Number is : ", Sum)



def main():
    X = int(input())
    Arr = []
    
    print("Enter Numbers in list : ")
    for i in range(0,X,1):
        value = int(input())
        Arr.append(value)

    print(Arr)

    evenlist = threading.Thread(target = EvenList ,args =(Arr,) )
    oddlist = threading.Thread(target = OddList ,args =(Arr,) )

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("Exit from main")

if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)
