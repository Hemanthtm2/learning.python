#!/usr/bin/python 


class DriverException(Exception):

  pass


drivers=[('Hemanth',28,),('Varada',25),('Achan',30),('Amma',27)]


for person,age in drivers:

   if age >= 35:
      driver=(person,age)
      print (driver)
      break

else:

   raise DriverException('Driver not found!')
