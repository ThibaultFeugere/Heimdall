#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

adresse, port = ("127.0.0.1", 5555)

username = raw_input("Quel est votre pseudo ?")

# Socket donnant l'accès au serveur
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_serveur.connect((adresse, port))
    print("Client " + username)
    # On envoie en bytes un message au serveur
    connexion_serveur.sendall(username.encode("utf8"))
except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    connexion_serveur.close()