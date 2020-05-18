#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

adresse, port = ("127.0.0.1", 5555)

# Socket donnant l'accès au serveur
connexion_with_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_with_serveur.connect((adresse, port))
    username = input("Quel est votre pseudo ?")
    print("Client " + username)
    # On envoie en bytes un message au serveur
    connexion_with_serveur.sendall(
        ("Je suis " + username + " et je me connecte").encode("utf8"))
    while (True):
        quitter = input("Souhaitez-vous vous déconnectez ? o/n")
        if(quitter == "o"):
            connexion_with_serveur.sendall(
                ("Je suis " + username + " et je me déconnecte").encode("utf8"))
            break
except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    connexion_with_serveur.close()
