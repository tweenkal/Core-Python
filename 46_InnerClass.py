# 👉Inner Class:-Class is a variable and method.inner class means
# class inside the class.
from tkinter.ttk import Style

# 👉Notes :- You can create the object of inner class inside the outer class.
# 👉you can create object of inner class outside the outer class provided
# you use outer class name to call it


class Student:     #outer class
    def __init__(self,name,rollno):
        # instance variable
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()   #Laptop class object is declare the outer class

    # instance method
    def show(self):
        print("Name=",self.name ,"Roll No=",self.rollno)
        self.lap.show()  #object of the show method

#     Inner class
    class Laptop:
        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i7"
            self.ram = 8

        # Instance method
        def show(self):
            print("Brand=",self.brand,"CPU=",self.cpu,"Ram=",self.ram)

s1 = Student("Twinkal",45)
s2 = Student("Hinal",89)

s1.show()
s2.show()

# lap1 = s1.lap
# print(id(lap1))
# lap2 = s2.lap
# print(id(lap2))

# directly create the object outside
# lap1 = Student.Laptop()
# lap2 = Student.Laptop()



