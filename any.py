#!/usr/bin/python

items=[0,None,True,0.0,7]

found=False


for item in items:

   print("Scanning item",item)

   if item:
     found=True
     break


if found:
   print("At least one item evalutes to True")

else:

   print("All items evalute to False")
