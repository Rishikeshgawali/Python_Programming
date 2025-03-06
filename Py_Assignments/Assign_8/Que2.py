#Write a recursive program which display below Pattern

def Fact(No):
    if(No != 1):
        No = No - 1
        Fact(No)
        print(No)

def main():
    Value = 5
    Fact(Value)

if __name__ == "__main__":
    main()

'''
Output : 
        1 2 3 4
    
'''