# string is palindrome or not

str = input("Enter string=")

if str == str[::-1]:
    print("palindrome")
else:
    print("Not palindrome")
