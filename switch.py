#!/usr/bin/python


day_number=int(input("Enter the day number\n"))


if 1 <= day_number <=5:
   day='Weekday'
   print(day)


elif day_number==6:
   day='Saturday'
   print(day)

elif day_number==0:
   day='Sunday'
   print(day)

else:

   day= ' '
   raise ValueError( str(day_number) + "is not a valid day number.")


