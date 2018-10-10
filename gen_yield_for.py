#!/usr/bin/python 


def print_squares(start,end):
    for x in range(start,end):
        yield x**2

for n in print_squares(2,5):
    print(n)
