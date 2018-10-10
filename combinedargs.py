#!/usr/bin/python


def combined(a,b=3,*c,**d):

   # print(a,b,c,d)
    print(a,d)

#combined(10,19,(1,2,3))


combined(50, **{'p':10,'q':20})
