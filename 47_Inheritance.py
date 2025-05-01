# 👉Inheritance:-
#👉Inheritance means the parent and child relationship
#👉Parent class is inherits to the child class menas parents property
# is also used and called the child property

# 👉Single level inheritance:- means the super class inherits the sub class

class A():   #Parent class
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):    #B is the child class for A
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

# explain single inheritence:-
# class A  :- feature 1 , feature 2
# class B  :- feature 3 , feature 4
# then class b is sub class it is inheriting the all the features the
# class a super class then
# class B:- feature 1 , feature 2 , feature 3 , feature 4

# 👉Multi level inheritance:-
# 👉it is one grand parent class , second is parent class and third is
# child class

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):   #Child class is B is inherites the parent class A
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B):     #Child class C is inherites the parent class of Class B
    def feature5(self):
        print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

c1 = C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

# 👉explanation of the multi-level inheritance:
# class c is inhetites the feature of class B and Class B is inherites
# the feature of Class A in shot Class C is inherites the Class A and
# Class B All the feature.
# class A -> feature1 , feature2
# class B -> feature 3 , feature 4
# class C -> feature5
# class A is a super class
# then class B ->feature1 , feature 2 ,feature 3, feature 4
# then class C -> feature1 , feature 2 ,feature 3, feature 4 , feature 5

# 👉Multiple Inheritance :- Class c is inherites the parent class A.
# and class B. one class extends to a multiple class

class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:   #Child class is B is inherites the parent class A
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):     #Child class C is inherites the parent class of Class B
    def feature5(self):
        print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

# explanation of the multiple inheritance:-
# Class C is inherites all the Class A and Class B Features but Class B
# is not inherites the Class A features.
