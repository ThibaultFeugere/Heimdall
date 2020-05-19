#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import

adresse, port = ("127.0.0.1", 5555)

login, home, fight, shop = False, False, False, False

# Socket donnant l'accès au serveur
connexion_with_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_with_serveur.connect((adresse, port))
    if not login:
        '''On charge la fenêtre de login / register'''
        login_register()
    if home:
        '''On charge la fenêtre principale'''
    if shop:
        '''On charge la fenêtre de la boutique'''
    if fight:
        '''On charge la fenêtre de combat'''
except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    connexion_with_serveur.close()
