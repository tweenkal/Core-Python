# 👉String is collection of multiple character and it is represent the '',"".
from numpy.ma.core import count

string = "Twinkle Pansuriya"

# 👉Upper case
print(string.upper())

# 👉Lower case
print(string.lower())

# 👉replace:-
print(string.replace("Twinkle","Jay"))

# 👉split:- it is convert to list
print(string.split(" "))

# 👉Capetlize :- it is string first character is capital
print(string.capitalize())

# 👉center():-this is print for the center for give the 50 space
print(string.center(50))

# 👉Count():- it is h is 2 time then it is count character 2
print(string.count("i"))

# 👉endswith():- it is give the string is end for the particular character
print(string.endswith("a"))
print(string.endswith("Pa",4,10))

# 👉find() :- search for the value
print(string.find("Pa"))
print(string.find("La"))  #not charcter and it is give -1

# 👉isalnum():- this string alpha numeric or not means A-Z , a-z  , 0-9
string2 = "TwinklePansuriya01"
# print(string2.isalnum())

print(string.isalnum())

# 👉isalpha :- it is not include number a-z , A-Z
print(string2.isalpha())

# 👉islower() :- all character is check lower case or not
print(string.islower())

# 👉isspace :- it is check the space is yes or no
str1 = "    "
print(str1.isspace())

# 👉istitle():-
print(string.istitle())

# 👉startwith() :- startwith is the start for the character or not
print(string.startswith("Twinkle"))

# 👉swapcase() :- it is upper to lower and lower to upper
print(string.swapcase())

# 👉title() :- it is covert for the title case
print(string.title())

