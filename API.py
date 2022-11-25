import socket
import utils
import ClientServerClass
import sys


serveur = ClientServerClass.Server()
client = ClientServerClass.Client()


#Fonction permetant d'initialiser la connection
def initialisation_communication(objet): 

	if (isinstance(objet, ClientServerClass.Client)) :
		client.connect()
	if (insinstace (objet, ClientServerClass.Serveur)) :
		serveur.start()


#Fonction permettant d'envoyer un fichier
def envoie(objet):

	if (isinstance(objet, ClientServerClass.Client) or insinstace (objet, ClientServerClass.Serveur)) :
		objet.send()
		
	
#Fonction permettant de recevoir 
def recevoir(objet): 

	if (isinstance(objet, ClientServerClass.Client) or insinstace (objet, ClientServerClass.Serveur)) :
		objet.receiveAll()


def fin_communication(objet,port):

	if (isinstance(objet, ClientServerClass.Client) or insinstace (objet, ClientServerClass.Serveur)) :
		objet.closeConnection()

