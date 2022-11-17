import socket
import utils

class Client :
    def __init__(self, port:int = 0, addr:str = None):
        #socket créé
        self.sock = socket.socket()
        self.port = port
        self.addr = addr

    def connect(self) :
        if (self.port != None and utils.checkValidIpAddress(self.addr) ) :
            self.sock.connect((self.addr, self.port))

    def sendString(self, message : str) :
        self.sock.send(message.encode())
    
    def closeConnection(self) :
        self.sock.close()

