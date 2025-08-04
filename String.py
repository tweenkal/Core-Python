# 👉slicing string
# 👉Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# output:- llo

# 👉Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
# output:-Hello

# 👉Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
# output:-llo, World!

# 👉From: "o" in "World!" (position -5)
# 👉To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
# output:-orl

# 👉capitalize:-	Converts the first character to upper case
# 👉Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
# output:-Hello, and welcome to my world.

# 👉casefold:-Converts string into lower case
# 👉Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
# output:-hello, and welcome to my world!

# 👉center:-Returns a centered string
# 👉Print the word "banana", taking up the space of 20 characters, with
# "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)
# output:-       banana

# 👉count:-Returns the number of times a specified value occurs in a string
# 👉Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
# output:-2

#👉 encode:-Returns an encoded version of the string
# 👉UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)
# output:-b'My name is St\xc3\xa5le'

# 👉endswith:-Returns true if the string ends with the specified value
# 👉Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# output:-True

# 👉expandtabs:-Sets the tab size of the string
# 👉Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
# output:-H e l l o

# 👉find:-Searches the string for a specified value and returns the position of where it was found
# 👉Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
# output:-7

#👉format:-Formats specified values in a string
# 👉Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# output:-For only 49.00 dollars!

# 👉index:-Searches the string for a specified value and returns the position of where it was found
# 👉Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
# output:-7

# 👉isalnum:-Returns True if all characters in the string are alphanumeric
# 👉Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)
# output:-True

# 👉isalpha:-Returns True if all characters in the string are in the alphabet
# 👉Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)
# output:-True

#👉isascii:-Returns True if all characters in the string are ascii characters
# 👉Check if all the characters in the text are ascii characters:
txt = "Company123"
x = txt.isascii()
print(x)
# output:-True

# 👉isdecimal:-Returns True if all characters in the string are decimals
# 👉Check if all the characters in a string are decimals (0-9):
txt = "1234"
x = txt.isdecimal()
print(x)
# output:-True

# 👉isdigit:-Returns True if all characters in the string are digits
# 👉Check if all the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x)
# output:-True

# 👉isidentifier:-Returns True if the string is an identifier
# 👉Check if the string is a valid identifier:
txt = "Demo"
x = txt.isidentifier()
print(x)
# output:-True

# 👉islower:-Returns True if all characters in the string are lower case
# 👉Check if all the characters in the text are in lower case:
txt = "hello world!"
x = txt.islower()
print(x)
# output:-True

# 👉isnumeric:-Returns True if all characters in the string are numeric
# 👉Check if all the characters in the text are numeric:
txt = "565543"
x = txt.isnumeric()
print(x)
# output:-True

# 👉isprintable:-Returns True if all characters in the string are printable
# 👉Check if all the characters in the text are printable:
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
# output:-True

#👉isspace:-Returns True if all characters in the string are whitespaces
# 👉Check if all the characters in the text are whitespaces:
txt = "   "
x = txt.isspace()
print(x)
# output:-True

#👉istitle:-	Returns True if the string follows the rules of a title
# 👉Check if each word start with an upper case letter:
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# output:-True

# 👉isupper:-Returns True if all characters in the string are upper case
# 👉Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
# output:-True

# 👉join:-Joins the elements of an iterable to the end of the string
# 👉Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# output:-John#Peter#Vicky

# 👉ljust:-Returns a left justified version of the string
# 👉Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
# output:-banana               is my favorite fruit.

# 👉lower:-Converts a string into lower case
# 👉Lower case the string:
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
# output:-hello my friends

# 👉lstrip:-Returns a left trim version of the string
# 👉Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
# output:-of all fruits banana      is my favorite

# 👉maketrans:-Returns a translation table to be used in translations
# 👉Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
# output:-Hello Pam!

#👉 partition:-Returns a tuple where the string is parted into three parts
# 👉Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
# output:-('I could eat ', 'bananas', ' all day')

# 👉replace:-Returns a string where a specified value is replaced with a specified value
# 👉Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
# output:-I like apples

# 👉rfind:-Searches the string for a specified value and returns the last position of where it was found
# 👉Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
# output:-12

#👉rindex:- Searches the string for a specified value and returns the last position of where it was found
#👉 Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
# output:-12

# 👉rjust:-Returns a right justified version of the string
# 👉Return a 20 characters long, right justified version of the word "banana":
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
# output:-              banana is my favorite fruit.

# 👉rpartition:-Returns a tuple where the string is parted into three parts
# 👉Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
# output:-('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

# 👉rsplit:-Splits the string at the specified separator, and returns a list
# 👉Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
# output:-['apple', 'banana', 'cherry']

#👉 rstrip:-Returns a right trim version of the string
# 👉Remove any white spaces at the end of the string:
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
# output:-of all fruits      banana is my favorite

# 👉split:-Splits the string at the specified separator, and returns a list
# 👉Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)
# output:-['welcome', 'to', 'the', 'jungle']

# 👉splitlines:-Splits the string at line breaks and returns a list
# 👉Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
# output:-['Thank you for the music', 'Welcome to the jungle']

# 👉startswith:-Returns true if the string starts with the specified value
#👉 Check if the string starts with "Hello":
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
# output:-True

# 👉strip:-Returns a trimmed version of the string
# 👉Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
# output:-of all fruits banana is my favorite

# 👉swapcase:-Swaps cases, lower case becomes upper case and vice versa
# 👉Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
# output:-hELLO mY nAME iS peter

# 👉title:-Converts the first character of each word to upper case
# 👉Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x)
# output:-Welcome To My World

#👉 translate:-Returns a translated string
# 👉Replace any "S" characters with a "P" character:
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
# output:-Hello Pam!

# 👉upper:-Converts a string into upper case
# 👉Upper case the string:
txt = "Hello my friends"
x = txt.upper()
print(x)
# output:-HELLO MY FRIENDS

# 👉zfill:-Fills the string with a specified number of 0 values at the beginning
#👉 Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)
# output:-0000000050

