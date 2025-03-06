import time
import threading

def DisplayEven(No):
    i = 0
    for i in range(0,(No*2),1):
        if (i%2 == 0):
            print("Even Number : ",i)

def DisplayOdd(No):
    i = 0
    for i in range(0,(No*2),1):
        if (i%2 != 0):
            print("Odd Number : ",i)


def main():
    x = int(input("Enter a Number to find the First X even and odd Numbers : "))

    even = threading.Thread(target = DisplayEven, args =(x,))
    odd = threading.Thread(target = DisplayOdd, args =(x,))

    even.start()
    odd.start()

    even.join()
    odd.join()


if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)
