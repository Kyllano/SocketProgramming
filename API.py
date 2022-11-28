import socket
import utils
import ClientServerClass
import sys


def creerInstance(typeInstance : str, port : int, addr : str = None) :
	if typeInstance.lower() == "server" or typeInstance.lower() == "serveur" :
		obj = ClientServerClass.Server(port)
	elif typeInstance.lower() == "client":
		if addr == None :
			print("Veuillez entrer une addresse de connexion distante valide")
			return None
		obj = ClientServerClass.Client(port, addr)
	else :
		print("Veuillez indiquer un type valide : client ou serveur")
		return None
	
	return obj

#Fonction permetant d'initialiser la connection
def initialisation_communication(objet): 
	if (isinstance(objet, ClientServerClass.Client)) :
		objet.connect()
		return 1
	elif (isinstance(objet, ClientServerClass.Serveur)) :
		objet.start()
		return 1
	else :
		print("L'instance donnée est invalide")
		return 0

#Fonction permettant d'envoyer un message
def envoie(objet, message : str):

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Serveur)) :
		objet.send(message.encode('utf-8'))
		
	
#Fonction permettant de recevoir 
def recevoir(objet): 

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Serveur)) :
		objet.receiveAll()


def fin_communication(objet):

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Serveur)) :
		objet.closeConnection()

