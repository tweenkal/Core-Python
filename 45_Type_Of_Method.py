# 👉Types of method:-
# 👉 Three type of method :- 1)class method 2)static method 3)Instance method
# 👉you know the class and static variable are same but class and static
# method is different in this method
# 👉if you remember instance is define self keyword.
# 👉instance method to work with the object.
# 👉instance method have two type 1)Accessor method 2)Mutator method
# 👉1)Accessor method :- it is only fetching the value.fetch the instance
# variable which will be used to the accessor.
# 👉2)Mutator method:- it is modify the value.
# 👉different variable is the different get and set method
# 👉three variable using the three method called the getters and setters.
# 👉getter :- getter is the get and fetch the value it not change the
# value like accessor.
# 👉setter :- setter is the set the value that can change the value like
# mutator.
# 👉class variable it takes the class method and instance variable
# it takes the instance method
# instance is use to the self key word and class is used to the class
# keyword means cls.
# 👉create a class method we need to use special symbol @ called decorator
# and mention the class method.
# 👉static method is not related to the object not related to the class
# its a blank no self no cls. and it is define the @ decorator static method.

class Student:

    school = "Telesko"   #class variable/static variable

    def __init__(self,m1,m2,m3):
        # instance variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    # instance method because is work with the object
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

#     fetch and get the m1 value
    def get_m1(self):
        return self.m1

#     set the m1 value
    def set_m1(self,value):
        self.m1 = value

#     class method is used to define the @ decorator
    @classmethod
    def get_School(cls):
        return cls.school

# static method is not related to the object not related to the class its a blank no self no cls.

    @staticmethod
    def info():
        print("This is the student class")

s1 = Student(67,45,34)
s2 = Student(89,67,89)

print("Avg1=",s1.avg())
print("Avg2=",s2.avg())

print("School=",Student.get_School())
Student.info()