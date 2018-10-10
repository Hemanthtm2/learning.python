#!/usr/bin/python

class Person:

   def __init__(self,age):
      self.age=age 




fab=Person(39)

print (fab.age)

print (id(fab)

fab.age=29

print (fab.age)

print (id(fab))
