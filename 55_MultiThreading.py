# 👉MultiThreading:-
# 👉breakdown for the software and each task is divide into multiple parts
# its called thread.
# 👉By-default every execution have a one thread that is known as main
# thread.that execution is done by have a main thread

from time import sleep
from threading import *

class Hello(Thread):

    def run(self):
        for i in range(0,5):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(0,5):
            print("HI")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("BYE")
# t1.run()
# t2.run()

