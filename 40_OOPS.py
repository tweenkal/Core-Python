# 👉Python support all different programing its support object
# oriented programing , functional programing and procedure programing.

# 👉procedure programing:- means the it is define the function and call
# the function it create the big big software and divided into small parts
# and break down the some modules.

# 👉functional programing :- means you can achieve a certain task
# implementing function as mathematical function where it is not
# manuplating the data exa..lambda

# 👉OOPS:-(objects)
# 👉objects is two things:-
# 1)every objects are certain attributes
# 2)every objects are certain behaviours.
# 👉objects are view something store data and object will have are some
# behaviour.
# 👉object are store some data where are used to the define variable.we
# are use define behaviour we need to use method

# 👉method :- when function  as object oriented programming it called
# as a method

# 👉OOPS concepts:-
# 1)object 2) class 3)Encapsulation 4)Polymorphism 5)Abstraction
# class - class is a design or that you can call a blueprint.class is a
# varibale and method
# object - instance of a class

# class and object
class Student:
    name = "karan"

s1 = Student()
print(s1.name)


# encapsulation
class Car:
    def __init__(self):
        self.__speed = 0  # Private variable

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10

    def get_speed(self):
        return self.__speed

# Using the class
my_car = Car()
my_car.accelerate()
my_car.accelerate()
print(my_car.get_speed())  # Output: 20
my_car.brake()
print(my_car.get_speed())  # Output: 10

