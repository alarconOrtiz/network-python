import socket

class Server(object):
    """docstring for ."""
    _PORT   = 1200
    _STATUS = 'IDLE'

    def __init__(self):
        super( self ).__init__()

   #methods to work with server.
    def Run_sever(self):
        print 'Server running'
        pass
    def Stop_sever(self):
        print 'Server stopped'
        pass
