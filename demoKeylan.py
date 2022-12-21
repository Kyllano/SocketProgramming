import API



serveur = API.creerInstance("server", 22222)

API.initialisation_communication(serveur)

API.envoie(serveur, "coucou Yon !")

print("[SERVEUR] J'ai recu : ", API.recevoir(serveur))

API.fin_communication(serveur)

