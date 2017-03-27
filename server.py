import socket

class Server( object ):
    """this class contains a server tcp where its port is given by a constructor"""
    #declararion of class variables


    def __init__( self, port ):
        self.port      = port
        self.__status_running_server = 0
        self.socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 & TCP

   #methods to work with server.
    def Run_sever( self ):
        __status_running_server = 1
        self.socket_fd.bind( ('', self.port) )
        self.socket_fd.listen( 5 )
        print 'ready to listen'
        while __status_running_server:
            socket_c, (host_c, puerto_c) = self.socket_fd.accept()
            print 'recived packet from client.'

        self.socket_fd.close()

    def Stop_sever( self ):
        __status_running_server = 0
