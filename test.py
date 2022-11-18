import ClientServerClass
import sys


"""
myClient = ClientServerClass.Client()
myClient.addr = "127.0.0.1"
myClient.port = 22222

myClient.connect()
#myClient.sendFile("./utils.py")
retour = myClient.receiveAll()
print("[CLIENT] J'ai recu tout mes machins! Mon retour :",retour)

myClient.closeConnection()
"""

myServer = ClientServerClass.Server()
myServer.port = 22222
conn, addr = myServer.start()

if (conn != None) :
    print("connection etablie ! Client est :")
    print(addr)
else :
    print("erreur :(")
    sys.exit(1)

myServer.sendString(conn, "Coucou!\n")
myServer.closeConnection(conn)
