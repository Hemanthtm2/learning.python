#!/usr/bin/python

def fibo(N):
 a,b=0,1

 while a <= N:
      yield a
      a,b=b,a+b


print(list(fibo(5)))
