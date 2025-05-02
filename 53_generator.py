# 👉generator:-
#👉 yield is the keyword which make a function as a generator.
#👉generator is give you the iterator
from setuptools.config.pyprojecttoml import validate


# def topten():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# values = topten()
# print(values.__next__())
# print(values.__next__())
#
# for i in values:
#     print(i)


def topten():

     n = 1

     while n <= 10:
         sq = n * n
         yield sq
         n += 1

values = topten()

for i in values:
    print(i)