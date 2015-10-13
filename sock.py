import socket

class mysocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            #self.sock.settimeout(0.0)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.port=port
        self.host=host
        self.sock.connect((host, port))

    def mysend(self, msg):
        self.msg=msg
        sent = self.sock.send(msg)

    def myreceive(self):
        result = ""

        data = self.sock.recv(1024)
        while len(data)>0 :
            result+=data
            data = self.sock.recv(1024)
        return result
