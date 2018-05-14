import sys
from server import Server

def main():
    print ('prueba de inicio de app en Python')
    my_server = Server(5000) #port 
    print ('Init server')
    my_server.Run_sever()

if __name__ == '__main__':
    main()
