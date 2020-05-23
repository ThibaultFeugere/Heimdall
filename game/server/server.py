#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
from game.server.database.login.login import Login


class ClientThread(threading.Thread):
    def __init__(self, connexion_client):
        threading.Thread.__init__(self)
        self.connexion_client = connexion_client

    def run(self):
        username = None
        password = None
        login = False
        while(True):
            # On attend de recevoir un message du du client
            data = self.connexion_client.recv(1024)
            data = data.decode("utf-8")
            if data != "":
                data = data.split(',')
                if data[0] == 'username':
                    username = data[1]
                if data[0] == 'password':
                    password = data[1]
            if login == False:
                if username and password and login == False:
                    login = Login(username, password).verify(Login(username, password).fetchPseudo())

#-------------------------------------------------

# AF_INET = adresses Internet de type IPv4
# SOCK_STREAM = protocole TCP
socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adresse, port = ("127.0.0.1", 5555)

# On lie le socket à une adresse et un port
socket_ecoute.bind((adresse, port))

print("Le serveur est démarré")

while True:
    # On met le socket à l'état d'écoute sur le port bindé
    socket_ecoute.listen(5)

    # On accepte la connexion du client
    connexion_client, adresse_client = socket_ecoute.accept()
    print(connexion_client, " et ", adresse_client)

    my_thread = ClientThread(connexion_client)
    my_thread.start()

# Fermeture des connexions
connexion_client.close()

# Fermeture du socket
socket_ecoute.close()
