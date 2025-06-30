# check leap year

year = int(input("Enter year="))

if(year % 4 == 0) and (year % 100 != 0 or year % 4 == 0):
    print("This is leap year")
else:
    print("This is not leap year")