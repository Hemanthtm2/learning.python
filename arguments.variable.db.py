#!/usr/bin/python


def connect(**options):
    conn_params={
         'host':options.get('host','127.0.0.1'),
         'port':options.get('port',11211),
         'user':options.get('user',''),
         'pwd':options.get('pwd',''),
         }
    print(conn_params)

connect()

connect(**{'host':'127.0.0.0','port':80,'user':'apache','pwd':'apache'})
