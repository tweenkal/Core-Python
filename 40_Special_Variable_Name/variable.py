# 👉Special variable is use for the _ _ (double underscore)
# 👉first module __name__ is always __main__ this will be code is start.

import Calc

# print(__name__)  #__main__  it is the starting point for the execution
#
# print("Hello" + __name__)
#
# print("Demo says=" + __name__)

def main():
    print("Hello")
    print("Welcome user")

if __name__ == "__main__":
    main()

