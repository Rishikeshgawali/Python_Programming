#Write a recursive program which display below Pattern

def Fact(No):
    if(No != 0):
        print(No)
        No = No - 1
        Fact(No)

def main():
    Value = 5
    Fact(Value)

if __name__ == "__main__":
    main()

'''
Output : 
        5 4 3 2 1
        
'''