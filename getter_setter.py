class Laptop:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self,new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("price must be positive!")


laptop = Laptop(2000)
print("current price:",laptop.get_price())
laptop.set_price(3000)
print("updated price:",laptop.get_price())
laptop.set_price(-8000)

# =========================================================================================
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        if new_name != " ":
            self.__name = new_name
        else:
            print("not is empty")


    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("not include negative")

emp = Employee("Twinkle",10000)
print("current name:",emp.get_name())
print("current salary:",emp.get_salary())

emp.set_name("Twinkle")
emp.set_salary(30000)
print("update name:",emp.get_name())
print("update salary",emp.get_salary())

emp.set_name(" ")
emp.set_salary(-6000)

# ============================================================================
import math

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self,value):
        if value > 0:
            self.__radius = value
        else:
            print("not include negative")

    def area(self):
        area = math.pi * self.__radius * self.__radius
        return area

c = Circle(5)
print("radius:",c.get_radius())
print("circle:",c.area())

c.set_radius(10)
print("radius:",c.get_radius())
print("circle:",c.area())

c.set_radius(-19)


# ==============================================================================

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,value):
        if value > 0 and value < 100:
            self.__marks = value

        else:
            print("only marks is 0-100")


    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
           return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"

s = Student(80)
print("Current marks:",s.get_marks())
print("Grade:",s.grade())

s.set_marks(90)
print("Updated marks",s.get_marks())
print("Grade:",s.grade())

s.set_marks(101)

# ==============================================================================

class Student:
    def __init__(self, name, rollno, marks):
        self.__name = name
        self.__rollno = rollno
        self.__marks = marks

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for roll number
    def get_rollno(self):
        return self.__rollno

    # Getter for marks
    def get_marks(self):
        return self.__marks

    # Setter for marks
    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Error: Marks must be between 0 and 100.")

    # Method to calculate grade
    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"

# Object creation
s = Student("Twinkle", 21, 80)

print("Name:", s.get_name())
print("Roll Number:", s.get_rollno())
print("Current Marks:", s.get_marks())
print("Grade:", s.grade())

s.set_marks(90)
print("\nUpdated Marks:", s.get_marks())
print("Grade:", s.grade())

s.set_marks(101)

# ================================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("❌ Age must be positive!")

# Example use
p1 = Person("Alice", 25)
print(p1.age)   # calls getter

p1.age = 30     # calls setter
print(p1.age)

p1.age = -5     # invalid
