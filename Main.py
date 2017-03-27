from server import Server

def Main():
    print 'prueba de inicio de app en Python'
    my_server = Server(50000) #port 
    print 'Init server'
    my_server.Run_sever()

if __name__ == '__main__':
    Main()
