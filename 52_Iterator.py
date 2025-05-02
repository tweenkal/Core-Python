# 👉Iterator:- iter() is a function to convert the list to iterator
# 👉iterator is not give all value it is give one value at a time
# 👉iter() is give the object of iterator
# 👉next() is the give the next value or object
from logging.config import stopListening

nums =  [4,5,6,7,8]
it = iter(nums)

print(it.__next__())    #4   #it is give me one next value at a time not give a all value

print(next(it))     #5

for i in nums:
    print(i)        #4,5,6,7,8



# 👉print top ten value

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val

        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)