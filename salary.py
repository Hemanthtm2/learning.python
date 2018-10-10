#!/usr/bin/python

salary=15000

if salary < 10000:
   tax=0.0
elif salary < 20000:
   tax=3.0
elif salary < 30000:
   tax=5.0
else:
   tax=10.0

print("My tax is",salary * tax,)
