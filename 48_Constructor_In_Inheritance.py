# 👉Constructor in inheritance:-
# 👉MRO(Method resolution order)
# 👉Sub class can access  all the features of super class. but  super
# class can not access any features of sub class

# class A:
#     # constructor of A
#     def __init__(self):
#         print("In A init")
#
#     def feature1(self):
#         print("feature 1 is working")
#
#     def feature2(self):
#         print("feature 2 is working")
#
# class B(A):
#     # constructor of B
#     def __init__(self):
#         super().__init__()  #this is the access the A Class
#         print("In B init")
#
#     def feature3(self):
#         print("feature 3 is working")
#
#     def feature4(self):
#         print("feature 4 is working")
#
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# 👉Note:= if you create object of sub class it will try  find init
# of sub class if it is not found then it will call init of super class

# 👉when you create object of sub class it will call init of sub class
# first.

# 👉super().__init__() using this
# 👉i am call the A and B both then use to the super keyword for then
# access the A. if you call have super then it will  first call  init
# of super class then call  init to sub class


class A:
    # constructor of A
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B:
    # constructor of B
    def __init__(self):
        print("In B init")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C Init")

    def feature5(self):
        print("feature 5 is working")

    def feat(self):
        super().feature2()     #MRO
a1 = C()
a1.feat()

# 👉problem :- this programme execute the and print the only the A
# and C class not print B Class then it is a problem then is used to
# the MRO.and MRO is work to for left to right

# 👉To represent the super class we use to the super method.

