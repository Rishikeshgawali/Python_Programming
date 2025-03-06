
class BookStore:

    No_of_Book = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author
        self.__class__.No_of_Book = self.No_of_Book + 1     #increment  class variable in __init__ method

    def Display(self):
        print("Name of book is : ",self.Name)
        print("Name of author is : ",self.Author)
        print("No of book is : ",self.No_of_Book)


def main():

    obj1 = BookStore("Linux System Programming ","Robert Love")
    obj1.Display()

    obj2 = BookStore("C programming","Dennis Ritchie")
    obj2.Display()



if __name__ == "__main__":
    main()

'''

Name of book is :  Linux System Programming
Name of author is :  Robert Love
No of book is :  1
Name of book is :  C programming
Name of author is :  Dennis Ritchie
No of book is :  2

'''
