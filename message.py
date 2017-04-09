import Frame from frame
class Message ( Frame ):
    """
    this class works like a basic structure to compose the format of the message .
    Message has several records:
        id = identifier per each client, forbiden 0 which is a Server ID
        command = it is a identifier of frame.
        payload = information of command.
        ??len   = length of frame recieved.
    """

    def __init__():
        self.arg     = arg
        self.id      = 0
        self.command = 0
        self.payload = 0

    def Create_message(id,command,payload):

        return Frame()

    def Get_InfoMesage():
        pass
