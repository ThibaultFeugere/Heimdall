import socket

# Socket donnant l'accès au serveur
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adresse, port = ("192.168.1.4", 5555)

# Demande de connexion au serveur
connexion_serveur.connect((adresse, port))

# On envoie en bytes un message au serveur
connexion_serveur.send(str.encode("Bonjour serveur !"))

# On ferme la connexion
connexion_serveur.close()
