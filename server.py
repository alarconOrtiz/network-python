import socket

class Server( object ):
    """docstring for ."""

    def __init__( self, port, status ):
        self.port   = port
        self.status = status

   #methods to work with server.
    def Run_sever( self ):
        print 'Server running'

    def Stop_sever( self ):
        print 'Server stopped'
