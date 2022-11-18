import ClientServerClass

myClient = ClientServerClass.Client()
myClient.addr = "127.0.0.1"
myClient.port = 22222

myClient.connect()
myClient.sendFile("./utils.py")
print("[CLIENT] J'ai envoyé mon fichier!\n", end='')

myClient.closeConnection()
