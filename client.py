import socket

class Client ( object ):
    """docstring for ."""
    _sock = None
    def __init__(self):
        global _sock
        #creating socket TCP/IP.
        _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def Connect( self, server_address, server_port ):
        #conection to the server.
        server_data = (server_address, server_port)
        _sock.connect(server_data)
        
    def Disconnect(self):
        #close the link with server.
        _sock.close()
        
    def SendInfo(self, frame):
        # this methos will take the class frame and 
        _sock.sendall(frame)
        
    def RecieveInfo(self):
        _sock.recv()
    
