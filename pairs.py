#!/usr/bin/python 


pairs=[]

items='ABCDE'

for a in range(len(items)):
    print(a)
    for b in range(a,len(items)):
        print(b)
        pairs.append((items[a],items[b]))

print(pairs)
