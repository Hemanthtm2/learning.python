#!/usr/bin/python

from time import time,sleep

def f(sleep_time=0.1):
    sleep(sleep_time)

def meassure(func,*args,**kwarg):
    t=time()
    func(*args,**kwarg)
    print(func.__name__,'took:',time()-t)


meassure(f)
meassure(f,0.5)
