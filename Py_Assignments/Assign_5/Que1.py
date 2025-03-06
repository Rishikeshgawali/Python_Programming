class Demo:

    Value = 0

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Value of First variable is : ",self.No1)
        print("Value of Second variable is : ",self.No2)

    def Gun(self):
        print("Value of First variable is : ", self.No1)
        print("Value of Second variable is : ", self.No2)


def main():

    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    print("After Call the Fun")
    obj1.Fun()
    obj2.Fun()

    print("After Call the Gun")
    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()

'''

After Call the Fun
Value of First variable is :  11
Value of Second variable is :  21
Value of First variable is :  51
Value of Second variable is :  101
After Call the Gun
Value of First variable is :  11
Value of Second variable is :  21
Value of First variable is :  51
Value of Second variable is :  101

'''
