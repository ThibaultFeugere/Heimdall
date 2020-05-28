#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
from database.login.login import Login
from database.register.register import Register


class ClientThread(threading.Thread):
    def __init__(self, connexion_client, number_online):
        threading.Thread.__init__(self)
        self.connexion_client = connexion_client
        self.number_online = number_online
        self.running = True

    def run(self):
        username = None
        password = None
        login = False
        register = False
        while(True):
            # On attend de recevoir un message du du client
            data = self.connexion_client.recv(1024)
            data = data.decode("utf-8")
            if data != "":
                data = data.split(',')
                if data[0] == 'login':
                    username = data[2]
                    password = data[4]
                    login = True
                if data[0] == 'register':
                    username = data[2]
                    password = data[4]
                    register = True

            if login:
                verify_login = Login(username, password).verify(
                    Login(username, password).fetchPseudo())
                if verify_login:
                    self.connexion_client.sendall(("1").encode("utf-8"))
                    self.connexion_client.sendall(
                        ("online, " + str(self.number_online)).encode("utf-8"))
                if not verify_login:
                    self.connexion_client.sendall(("0").encode("utf-8"))
                login = False
            if register:
                verify_register = Register(username, password).register()
                if verify_register:
                    self.connexion_client.sendall(("1").encode("utf-8"))
                if not verify_register:
                    self.connexion_client.sendall(("0").encode("utf-8"))
                register = False

    def stop(self):
        self.running = False
# -------------------------------------------------


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
    print(threading.activeCount())
    my_thread = ClientThread(connexion_client, threading.active_count())
    my_thread.start()

# Fermeture des connexions
connexion_client.close()

# Fermeture du socket
socket_ecoute.close()
