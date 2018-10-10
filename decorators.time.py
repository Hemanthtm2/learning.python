#!/usr/bin/python

from time import time,sleep

def f():
    sleep(.3)


def g():
    sleep(.5)


f()
t=time()
print('f took:',time()-t)

g()
t=time()

print('g took:',time() -t)
