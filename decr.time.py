#!/usr/bin/python
from time import time,sleep

def f():
    sleep(.3)

def g():
    sleep(.5)


def meassure(func):
    t=time()
    func()
    print(func.__name__,'took:',time()-t)


meassure(f)
meassure(g)
