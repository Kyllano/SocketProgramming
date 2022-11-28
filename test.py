import ClientServerClass
import sys
import API


client = API.creerInstance("client", 22222, "localhost")
API.initialisation_communication(client)
API.envoie(client, "hello!")
print(API.recevoir(client))
API.fin_communication(client)


"""
myClient = ClientServerClass.Client()
myClient.addr = "127.0.0.1"
myClient.port = 22222

myClient.connect()
#myClient.sendFile("./utils.py")
retour = myClient.receiveAll()
print("[CLIENT] J'ai recu tout mes machins! Mon retour :",retour)

myClient.closeConnection()

myServer = ClientServerClass.Server()
myServer.port = 22222
addr = myServer.start()

if (myServer.conn != None) :
    print("connection etablie ! Client est :")
    print(addr)
else :
    print("erreur :(")
    sys.exit(1)

myServer.sendString("Coucou!\n")
myServer.closeConnection()

myServer.start()

print("reconnexion effectuée")

myServer.closeConnection()
"""