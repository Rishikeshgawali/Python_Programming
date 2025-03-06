'''
Create on module named as Arithmetic which contains 4 functions as Add(),Sub(),Mult(),Div() .All functions Accept 2 parameters as number and 
perform the operation. Write python program which call all the functions from Arithmetic module by Acccepting the parmeters from user.
'''

import Arithmetic       #module name

def main():

    print("Enter First Number :")
    x = input()

    print("Enter Second Number :")
    y = input()

    Ans1 = Arithmetic.Add(int(x),int(y))
    print("Addition of {0} and {1} is : {2}".format(x,y,Ans1))

    Ans2 = Arithmetic.Sub(int(x),int(y))
    print("Substraction of {0} and {1} is : {2}".format(x,y,Ans2))

    Ans3 = Arithmetic.Mult(int(x),int(y))
    print("Multiplication of {0} and {1} is : {2}".format(x,y,Ans3))

    Ans4 = Arithmetic.Div(int(x),int(y))
    print("Division of {0} and {1} is : {2}".format(x,y,Ans4))

if __name__ == "__main__":
    main()

'''
Output : 

Enter First Number :
10
Enter Second Number :
5
Addition of 10 and 5 is : 15
Substraction of 10 and 5 is : 5
Multiplication of 10 and 5 is : 50
Division of 10 and 5 is : 2.0
'''