#!/usr/bin/python

from itertools import compress

data=range(100)

even_selector=[1,0]*100
odd_selector=[0,10]*100


even_num=list(compress(data,even_selector))

odd_num=list(compress(data,odd_selector))


print(even_num)

print(odd_num)

