#!/usr/bin/python

from time import time 

mx=2*10**7

t=time()
absloop=[]

for n in range(mx):
    absloop.append(abs(n))

print('for loop: {:4f} s'.format(time() -t))


t=time()

abslist=[abs(n) for n in range(mx)]

print('list comprehension: {:4f} s'.format(time()-t))


t=time()

absgen=list(abs(n) for n in range(mx))

print('Generator expression: {:4f} s'.format(time() -t))
