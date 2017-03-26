import socket

class Server( object ):
    """docstring for ."""
    #declararion of class variables
    _status_running_server = 0 #false

    def __init__( self, port, status ):
        self.port      = port
        self.status    = status
        self.socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 & TCP

   #methods to work with server.
    def Run_sever( self ):
        _status_running_server = 1
        self.socket_fd.bind( 'localhost', self.port )
        self.socket_fd.listen( 5 )
        print 'ready to listen'
        while _status_running_server:
            socket_c, (host_c, puerto_c) = self.socketfd.accept()
            print 'recived packet from client.'

        socketfd.close()

    def Stop_sever( self ):
        _status_running_server = 0
