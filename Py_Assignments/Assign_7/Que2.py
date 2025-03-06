import time
import threading

def EvenFact(No):
    for i in range(2,(No//2)+1):
        if(No % i == 0 and i % 2 == 0):
            print("Even Factorial is : ",i)

def OddFact(No):
    for i in range(2,(No//2)+1):
        if(No % i == 0 and i % 2 != 0):
            print("Odd Factorial is : ",i)


def main():
    X = int(input("Enter a Number: "))

    evenfactor = threading.Thread(target = EvenFact , args = (X,))
    oddfactor = threading.Thread(target = OddFact , args = (X,))

    evenfactor.start()
    oddfactor.start()
    
    evenfactor.join()
    oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)
