#!/usr/bin/python

from math import sqrt

mx=10

leg=[(a,b,sqrt(a**2+b**2)) for a in range(1,mx) for b in range(a,mx)] 

print(leg)

leg=list(filter(lambda triple: triple[2].is_integer(),leg))

print(leg)
