# 👉Polymorphism :- is break down the word poly + morphism .poly means
# many and morph means form that means one think can multiple forms.objects
# have multiple form
# 👉4 ways of implementing polymorphism
# 👉1)duck typing 2)operator overloading
# 3)method overloading 4)method overriding.

# 👉Duck typing:-
# 👉means this is a bird is walking like a duck , swimming like a duck and
# quacks like a duck that it is probably bird is a duck


class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditior:

    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = MyEditior()

lap1 = Laptop()
lap1.code(ide)

# 👉Operator Overloading:-same method but argument are different

a = '5'
b = '6'

print(a+b)
print(str.__add__(a,b))


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):    #add is the buit in function
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

    def __gt__(self, other):   #gt means grater than
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.m1,self.m2)

s1 = Student(89,78)
s2 = Student(66,38)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
print(s2)

# 👉Method overloading :- is not there in python means two method have a
# same name but argument must be different.

# 👉method overriding :- same name and same parameter