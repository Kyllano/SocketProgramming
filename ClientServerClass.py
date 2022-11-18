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

    #Permet d'envoyer des informations quelconques, nécessites qu'elles soient sous forme de bytes
    def send(self, message : bytes) :
        self.sock.send(message)

    #Permet d'envoyer une chaine de caractère
    def sendString(self, message : str) :
        self.sock.send(message.encode())

    #Permet d'envoyer un fichier en tant que bytes, nécessite que le fichier existe
    def sendFile(self, filename) :
        try:
            file = open(filename, 'rb')
        except OSError :
            print("Ouverture du fichier impossible : ", filename)
            return False
        
        content = file.read()
        self.sock.sendall(content)
        file.close()
        

    #Permet de recevoir une chaine de caractère courte, idéale pour tester une connexion
    def receiveShortString(self) :
        message = self.sock.recv(1024)
        return message.decode()

    #Permet de recevoir jusque 4096 bytes envoyés. Due au fait que généralement, les longs message ne sont pas des strings, il est à l'utilisateur de décoder l'information
    def receive(self) :
        message = self.sock.recv(4096)
        return message

    #Permet de recevoir un fichier envoyé
    def receiveFileInfos(self, filename) :
        file = open(filename, 'wb')
        while True :
            recvfile = self.sock.recv(4096)
            if not recvfile : break
            file.write(recvfile)
        file.close()
    
    def closeConnection(self) :
        self.sock.close()

class Server :
    def __init__(self, port:int):
        self.sock = None
        self.port = port
        
    #Permet de lancer le serveur
    def start(self) :
        if (utils.checkValidPort(self.port)) :
            try :
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error as err :
                print("Creation du socket impossible : %s"%(err))
                return None

            self.sock.bind(('', self.port)) #Socket connecté au port
            self.sock.listen(5) #On écoute et on met 5 requêtes de connections en attente avant de refuser (5 étant la norme)
            conn, addr = self.sock.accept()
            return conn,addr
        else :
            print("Numero de port invalide")
            return None
    

