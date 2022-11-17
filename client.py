import socket
import utils

class Client :
    def __init__(self, port:int = 0, addr:str = None):
        #socket créé
        self.sock = socket.socket()
        self.port = port
        self.addr = addr

    #Permet de se connecter a un server
    def connect(self) :
        if (self.port != None and utils.checkValidIpAddress(self.addr) ) :
            self.sock.connect((self.addr, self.port))
        else :
            print("[CLIENT] Connexion impossible, le numéro de port ou ")

    def sendString(self, message : str) :
        self.sock.send(message.encode())

    def receiveShortString(self) :
        message = self.sock.recv(1024)
        return message.decode()
    
    def closeConnection(self) :
        self.sock.close()

