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
		return objet.connect()
	elif (isinstance(objet, ClientServerClass.Server)) :
		return objet.start()
		
	else :
		print("L'instance donnée est invalide")
		return 0

#Fonction permettant d'envoyer un message
def envoie(objet, message : str):

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Server)) :
		objet.send(message.encode('utf-8'))
	else :
		print("L'instance données est invalide")
		return None
		
	
#Fonction permettant de recevoir 
def recevoir(objet): 

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Server)) :
		return objet.receiveAll().decode('utf-8')
	else :
		print("L'instance données est invalide")
		return None


def fin_communication(objet):

	if (isinstance(objet, ClientServerClass.Client) or isinstance(objet, ClientServerClass.Server)) :
		objet.closeConnection()
		return 0
	else :
		print("L'instance données est invalide")
		return None

