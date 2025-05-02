# 👉Library:-
# 👉internal library :-means not install any library
# 👉1)random 2)calender 3)math 4)map 5)lambda 6)re

# 👉2)external library:-means install the library.
#1)QR code 2)GTTS library :-text convert to audio

# 👉random int:-
# this random is the print the random element in for the specific limit
# This is use for the otp , dice , capcha code.
import random
from logging import fatal
from math import factorial
from random import shuffle

from qrcode.main import QRCode

print(random.randint(0,70))

# 👉random sample:- it is give the random simple list ,string etc...
# 👉sample is give me the output for the list form
# 👉It is not support int and float
# 👉it is the pre-define library.
# 👉it not change the actual list

a = [1,"hello","hii",8.8,True]
print(random.sample(a,5))

b = "abcdefghij"
print(random.sample(b,5))

# 👉random shuffle :- it is not give the limit.it is the change the
# sequance.it change the full list.it not fix the position it is every
# time change
# 👉it change the actual list
# 👉shuffle is not work for the string

a = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
shuffle(a)
print(a)

# 👉print and generate the capcha code

a = "uyetghjyihsa"
b = "123456783"
c = "#$%@&*^~*()"

# using concatenate string.
# print("".join(random.sample(a,4))+"".join(random.sample(b,3))+"".join(random.sample(c,5)))

# print single line not a next line first method
print("".join(random.sample(a,4)),end="")
print("".join(random.sample(b,3)),end="")
print("".join(random.sample(c,5)))

# 👉change the sequeance using shuffle

a = (random.sample(a,4)) + (random.sample(b,3)) + (random.sample(c,5))
random.shuffle(a)
print("".join(a))

# 👉join():-it is join string to each other elements.

# 👉2)calender :- print the calender but import calender

import calendar

print(calendar.calendar(2025))
print(calendar.isleap(2023))  #is check the leap year or not

# 👉3)math() :- using mathematics function

import  math
print(factorial(5))
print(math.sqrt(24))
print(math.floor(9.0))       #it is return to int and as it is value before the point
print(math.ceil(8.2))   #it is the increment value one it doesnt metter the after the point value


# 👉4)map() :- work for the multiple value .

a = ["sunday","monday","tuesday","Wednesday"]
b = list(map(list,a))
print(b)

# 👉lambda() :- it is anonymous function.no function name

a = lambda x:x*x*x
print(a(2))

c = lambda x,y : x + y
print(c(3,4))

# 👉lambda and map ek sathe

a = [1,2,4,5,6,6]
b = [4,6,7,5,4,2]

c = list(map(lambda x,y : x + y,a,b))
print(c)

# 👉re means regular expression

# import re
# a = ['0-9|a-p']
# print(a)

# 👉QR C0de:-
# 👉make() :- means make simple QR code
# 👉add_data means the color change QR code and border width

import qrcode

qr = qrcode.make("https://www.python.org/")
qr.save('qr.png')

qr2 = qrcode.make("https://www.youtube.com/")
qr2.save('youtube.jpg')

# 👉make color full QR code

qr = qrcode.QRCode(box_size=10,border=6)
qr.add_data("https://www.python.org/")
img = qr.make_image(fill_color='blue',back_color='white')
img.save('qr.png')

# 👉GTTS:- this make the audio
from gtts import gTTS

tts = gTTS("Hello python")
tts.save("audio.mp3")

# 👉scan the qrcode and show the text

img = qrcode.make("Some text here")
img.save('text.png')