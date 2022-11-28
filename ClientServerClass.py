import socket
import utils

class Client :
    #Permet de prendr en nom de domaine ou une addresse IP
    def __init__(self, port:int = 0, addr:str = None):
        #socket créé
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.addr = addr

    #Permet de se connecter a un server
    def connect(self) :
        if self.addr == None :
            print("[SERVER] Veuillez indiquer une addresse valide")
            return -1
        try :
            self.addr = socket.gethostbyname(self.addr)
        except socket.gaierror as e:
            print(f'[CLIENT] Nom de domaine invalide : {e}')
            return -2
        if (self.port == None or not utils.checkValidIpAddress(self.addr)) :
            print("[CLIENT] Connexion impossible, le numéro de port ou l'addresse est invalide")
            return -3

        try :
            self.sock.connect((self.addr, self.port))
            return 0
        except socket.timeout :
            print("[CLIENT] Timeout")
            return -4


    #Permet d'envoyer des informations quelconques, nécessites qu'elles soient sous forme de bytes
    def send(self, message : bytes) :
        return self.sock.send(message)

    #Permet d'envoyer une chaine de caractère
    def sendString(self, message : str) :
        return self.sock.send(message.encode())

    #Permet d'envoyer un fichier en tant que bytes, nécessite que le fichier existe
    #Retourne None en cas d'erreur et la longueur du fichier envoyé en cas de reussite
    def sendFile(self, filename) :
        try:
            file = open(filename, 'rb')
        except OSError :
            print("[CLIENT] Ouverture du fichier impossible : ", filename)
            return None
        
        content = file.read()
        self.sock.sendall(content)
        file.close()
        return len(content)
        

    #Permet de recevoir une chaine de caractère courte, idéale pour tester une connexion
    def receiveShortString(self) :
        message = self.sock.recv(1024)
        return message.decode()

    #Permet de recevoir jusque 4096 bytes envoyés. Due au fait que généralement, les longs message ne sont pas des strings, il est à l'utilisateur de décoder l'information
    def receive(self) :
        message = self.sock.recv(4096)
        return message
    
    #Permet de recevoir des messages de tailles indeterminés. Ici aussi, on n'effetue pas de traitement sur l'information, on ne fait que la recevoir
    def receiveAll(self) :
        TaillBuff = 4096
        data = b''
        while True :
            recv = self.sock.recv(4096)
            data += recv
            if (len(recv) < TaillBuff) :
                break
        return data

    #Permet de recevoir un fichier envoyé
    #retourne la taille du fichier ou None si erreur
    def receiveFile(self, filename) :
        try:
            file = open(filename, 'wb')
        except OSError :
            print("[CLIENT] Ouverture du fichier impossible : ", filename)
            return None

        TaillBuff = 4096
        taille = 0
        while True :
            recvfile = self.sock.recv(4096)
            file.write(recvfile)
            taille += len(recvfile)
            if (len(recvfile) < TaillBuff) :
                break
        file.close()
        return taille
    
    def closeConnection(self) :
        self.sock.close()

class Server :
    def __init__(self, port:int = None):
        self.sock = None
        self.port = port
        self.conn = None

    #Permet de lancer le serveur
    def start(self) :
        if (not utils.checkValidPort(self.port)) :
            print("[SERVEUR] Numero de port invalide")
            return -1

        if (self.sock == None) :
            try :
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except socket.error as err :
                print("[SERVEUR] Creation du socket impossible : %s"%(err))
                return -2

            self.sock.bind(('', self.port)) #Socket connecté au port

        self.sock.listen(5) #On écoute et on met 5 requêtes de connections en attente avant de refuser (5 étant la norme)
        self.conn, addr = self.sock.accept()
        return addr

    
    #Permet d'envoyer des informations quelconques, nécessites qu'elles soient sous forme de bytes
    def send(self, message : bytes) :
        return self.conn.send(message)

    #Permet d'envoyer une chaine de caractère
    def sendString(self, message : str) :
        return self.conn.send(message.encode())

    #Permet d'envoyer un fichier en tant que bytes, nécessite que le fichier existe
    #Retourne None en cas d'erreur et la longueur du fichier envoyé en cas de reussite
    def sendFile(self, filename : str) :
        try:
            file = open(filename, 'rb')
        except OSError :
            print("Ouverture du fichier impossible : ", filename)
            return None
        
        content = file.read()
        self.conn.sendall(content)
        file.close()
        return len(content)

    #Permet de recevoir une chaine de caractère courte, idéale pour tester une connexion
    def receiveShortString(self) :
        message = self.conn.recv(1024)
        return message.decode()

    #Permet de recevoir jusque 4096 bytes envoyés. Due au fait que généralement, les longs message ne sont pas des strings, il est à l'utilisateur de décoder l'information
    def receive(self) :
        message = self.conn.recv(4096)
        return message
    
    #Permet de recevoir des messages de tailles indeterminés. Ici aussi, on n'effetue pas de traitement sur l'information, on ne fait que la recevoir
    def receiveAll(self) :
        TaillBuff = 4096
        data = b''
        while True :
            recv = self.conn.recv(4096)
            data += recv
            if (len(recv) < TaillBuff) :
                break
        return data

    #Permet de recevoir un fichier envoyé
    #retourne la taille du fichier ou None si erreur
    def receiveFile(self, filename) :
        try:
            file = open(filename, 'wb')
        except OSError :
            print("Ouverture du fichier impossible : ", filename)
            return None

        TaillBuff = 4096
        taille = 0
        while True :
            recvfile = self.conn.recv(4096)
            file.write(recvfile)
            taille += len(recvfile)
            if (len(recvfile) < TaillBuff) :
                break
        file.close()
        return taille

    def closeConnection(self) :
        if self.conn != None :
            self.conn.close()
            self.conn = None