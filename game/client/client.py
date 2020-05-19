#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket


class Client():

    def __init__(self, pseudo, password):
        self.pseudo = pseudo
        self.password = password
        self.connexion_with_serveur = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

    def connexionServeur(self):
        adresse, port = ("127.0.0.1", 5555)

        # Socket donnant l'accès au serveur

        try:
            # Demande de connexion au serveur
            self.connexion_with_serveur.connect((adresse, port))
            self.SayHello()
            while (True):
                quitter = input("Souhaitez-vous vous déconnectez ? o/n")
                if(quitter == "o"):
                    self.SayBye()
                    break
        except ConnectionRefusedError:
            print("Connexion au serveur échouée")
        finally:
            # On ferme la connexion
            self.connexion_with_serveur.close()

    def SayHello(self):
        # On envoie en bytes un message au serveur
        self.connexion_with_serveur.sendall(
            ("Je suis " + self.pseudo + " et je me connecte").encode("utf8"))

    def SayBye(self):
        # On envoie en bytes un message au serveur
        self.connexion_with_serveur.sendall(
            ("Je suis " + self.pseudo + " et je me déconnecte").encode("utf8"))


# test = Client('Hades', 'password')
# test.connexionServeur()
