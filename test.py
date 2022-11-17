import client
import utils

myClient = client.Client()
myClient.addr = "127.0.0.1"
myClient.port = 22222

myClient.connect()
mess = myClient.receiveShortString()
print("[CLIENT] J'ai recu :", mess, end='')

myClient.closeConnection()
