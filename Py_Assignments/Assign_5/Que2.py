
class Circle:

    PI = 3.14

    def __init__(self):
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0


    def Accept(self):
        print("Enter the value of Radius : ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = self.PI*self.Radius*self.Radius


    def CalculateCircumference(self):
        self.Circumference = 2*self.PI*self.Radius


    def Display(self):
        print("Value of Radius is : ",self.Radius)
        print("Value of Area is : ",self.Area)
        print("Value of Circumference is : ",self.Circumference)


def main():
    obj1 = Circle()
    obj2 = Circle()

    print("Accept Info. for 1st Object")
    obj1.Accept()
    print("Accept Info. for 2nd Object")
    obj2.Accept()

    obj1.CalculateArea()
    obj1.CalculateCircumference()
    print("Information of First Object is : ")
    obj1.Display()
    print("\n")

    obj2.CalculateArea()
    obj2.CalculateCircumference()
    print("Information of Second Object is : ")
    obj2.Display()

if __name__ == "__main__":
    main()

'''

Accept Info. for 1st Object
Enter the value of Radius :
4
Accept Info. for 2nd Object
Enter the value of Radius :
5
Information of First Object is :
Value of Radius is :  4.0
Value of Area is :  50.24
Value of Circumference is :  25.12


Information of Second Object is :
Value of Radius is :  5.0
Value of Area is :  78.5
Value of Circumference is :  31.400000000000002

'''