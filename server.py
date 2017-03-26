import socket

class Server( object ):
    """docstring for ."""
    #declararion of class variables
    _status_running_server = 0 #false

    def __init__( self, port, status ):
        self.port      = port
        self.status    = status
        self.socket_fd = socket.Socket()

   #methods to work with server.
    def Run_sever( self ):
        _status_running_server = 1
        socket_fd.bind( 'localhost', self.port )
        socket_fd.listen( 5 )
        while _status_running_server:
            socket_c, (host_c, puerto_c) = socketfd.accept()
            print 'recived packet from client.'
        socketfd.close()

    def Stop_sever( self ):
        _status_running_server = 0
