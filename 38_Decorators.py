# 👉Decorators:-
# 👉Using Decorators add the extra features in for existing function

def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper()

@my_decorator
def hello():
    print("hello world")

hello()