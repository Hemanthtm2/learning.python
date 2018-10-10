#!/usr/bin/python


class DriverException(Exception):

   pass


people=[('James',17),('Kirk',9),('Lara',13),('Robert',8),('Hemanth',28)]
driver=None

for person,age in people:
    if age>=18:
      driver=(person,age)
      print(driver)
      break

if driver is None:

   raise DriverException('Driver not Found.')
