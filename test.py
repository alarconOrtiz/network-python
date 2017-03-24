import os
from communication import server

def Main():
    print 'prueba de inicio de app en Python'
    my_server = server()
    print 'Init server'
    my_server.Run_sever()

if __name__ == '__main__':
    Main()
