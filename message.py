import Frame from frame
class Message ( Frame ):
    """
    this class works like a basic structure to compose the format of the message .
    Message has several records:
        id      = identifier per each client, forbiden 0 which is a Server ID
        command = it is a identifier of frame.
        payload = information of command.
        len     = length of frame recieved.
    """

    def __init__( self ):
        self.mId_src  = 0
        self.mId_dst  = 0
        self.mLen     = 0
        self.mCommand = 0
        self.mPayload = 0

    def Create_message( self, id_src, id_dst, command, payload):
        data = [len, id_dst, id_src, command, payload]
        return Frame(data)

    def Get_InfoMesage( self, frame ):
        mLen    = frame.dataFrame[0]
        mId_dst = frame.dataFrame[1]
        mId_src = frame.dataFrame[2]
        mCommand= frame.dataFrame[3]
        mPayload= frame.dataFrame[4]
