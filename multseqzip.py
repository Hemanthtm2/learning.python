#!/usr/bin/python

brands=['Adidas','Puma','Nike','Reebok','Fila']
ratings=[5,4,4,3,3]
countries=['Germany','Germany','America','America','England']
for brand,rate,country in zip(brands,ratings,countries):

    print(brand,'\t''|''\t',rate,'\t''|','\t',country)
