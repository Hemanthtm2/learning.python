#!/usr/bin/python 


n=int(input("Enter the number you wish to get the binary!!!\n"))

rems=[]

while n > 0:

   rem=n%2
   rems.append(rem)
   n=n//2

rems=rems[:: -1]

print(rems)
   
