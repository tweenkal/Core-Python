# 👉Global keyword(variable) :- means it is declare the variable for
# outside of the function its called the global keyword.

# 👉local keyword(variable) :- means it is declare variable for inside the
# function its called the local keyword


a = 10    #global

def func():
    global a
    a = 15    #Local
    print("Outside of the function",a)

func()

print("Outside of the function",a)


# 👉here i am local variable is access to 15 and global variable is access
# the 10 but i am remove the local variable a = 15 then it is access
# the by-default the global variable.and it is access the global
# variable inside the function as well.

# 👉but i am inside the function is not used the local variable for use
# the i am global variable then it is used to the global keyword.


# 👉using globals() function:-
a = 10
print(id(a))

def something():
    a = 9

    x = globals()['a']
    print(id(x))
    print("inside function=",a)

    globals()['a'] = 15

something()

print("Outside of the function=",a)
