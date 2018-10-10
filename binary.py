#!/usr/bin/python 


num=int(input("Enter the number you want in binary format!!! \n"))


remainders=[]

while num > 0:

   remainder=num % 2
   remainders.append(remainder)
   num=num//2

remainders=remainders[:: -1]

print(remainders)
   
