import API



client = API.creerInstance("client", 22222)

API.initialisation_communication(client)

print("[CLIENT] J'ai recu : ", API.recevoir(client))

API.envoie(client, "Salut Keylan !")

API.fin_communication(client)

