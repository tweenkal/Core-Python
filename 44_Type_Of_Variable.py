# 👉Two type of variable:-
# 1)Static variable(class variable) 2)Instance variable
#👉 It is define the inside init is called a instance variable
# 👉It is define the outside init is called a class variable.
# 👉memory are different namespace namespace means create and store the
# object / variable.
# 👉Two type of namespace:-
# 1)Class namespace :- it store the all the class variable
# 2)object / instance namespace :-its create all instance variable

# 👉here outside the init class variable we will change the value then it
# is affecting to each another variable

# 👉here inside the init instance variable we will change the value then
# it is not affecting to each another variable

class car:

    wheels = 4          #class variable  or namespace

    def __init__(self):
        self.mil = 10               #Instance variable  or namespace
        self.name = "BMW"

c1 = car()
c2 = car()

c1.mil = 8

print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)

