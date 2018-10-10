#!/usr/bin/python 


def outer():
   test=1
   def inner():
       nonlocal test
       test=2
       print("Inner",test)
   inner()
   print("Outer",test)

test=0

outer()
print("Global",test)

