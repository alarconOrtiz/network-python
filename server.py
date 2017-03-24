import socket

class Server(object):
    """docstring for ."""

    def __init__(self, port, status):
        super( self ).__init__()
        self.port   = port
        self.status = status

    def __init__(self):
        super( self ).__init__()
        self.port   = 6666
        self.status = 'IDLE'

   #methods to work with server.
    def Run_sever(self):
        print 'Server running'
        pass
    def Stop_sever(self):
        print 'Server stopped'
        pass
