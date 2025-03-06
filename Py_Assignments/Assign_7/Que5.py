import time
import threading

def Display(No):
    i = 0
    for i in range(1,No+1):
        print("Value is in Display: ",i)


def DisplayReverse(No):
    i = 0
    for i in range(No,0,-1):
        print("Value is in DisplayReverse : ",i)


def main():
    X = 50

    Thread1 = threading.Thread(target =Display , args = (X,))
    Thread2 = threading.Thread(target =DisplayReverse , args = (X,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)
