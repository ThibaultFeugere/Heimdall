#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame, math, time, datetime, socket
from game import Game
import buttons.buttons as button
import stop as Stop

adresse, port = ("127.0.0.1", 5555)
Login = None

# Socket donnant l'accès au serveur
connexion_with_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_with_serveur.connect((adresse, port))

    # Demande de connexion ou d'enregistrement
    print("1 - Se connecter\n")
    print("2 - S'enregistrer\n")
    print("3 - Quitter\n")
    answer = input("Que souhaitez-vous faire (1, 2 ou 3) ?\n")

    # Connexion
    if answer == "1":
        username = input("Quel est votre pseudo ?\n")
        password = input("Quel est votre mot de passe ?\n")
        connexion_with_serveur.sendall(("login, username," + username + ", password," + password).encode("utf8"))
        data = connexion_with_serveur.recv(1024)
        Login = data.decode("utf-8")
        data = connexion_with_serveur.recv(1024)
        number_online = data.decode("utf-8")
        print(number_online)
    if answer == "2":
        username = input("Quel est votre pseudo ?\n")
        password = input("Veuillez saisir un mot de passe\n")
        second_password = input("Veuillez resaisir le mot de passe\n")

        if password == second_password:
            connexion_with_serveur.sendall(("register, username," + username + ", password," + password).encode("utf8"))
            data = connexion_with_serveur.recv(1024)
            verify_register = data.decode("utf-8")
            data = connexion_with_serveur.recv(1024)
            number_online = data.decode("utf-8")
            print(number_online)
            print(verify_register)
            if verify_register == "1":
                Login = verify_register
            if verify_register == "0":
                print("Le pseudo existe déjà...")
                Login = "0"
        else:
            print("Les deux mot de passes ne correspondent pas...")

    if answer == "3":
        Stop.stop(connexion_with_serveur)

    if answer != "1" and answer !="2" and answer !="3":
        # Il faut reappeler la fonction qui pose les questions
        Stop.stop(connexion_with_serveur)

    if Login == "0":
        print("Login echoué")
        Stop.stop(connexion_with_serveur)

    if Login == "1":
        print("Login effectué avec succès !")

        pygame.init()
        pygame.font.init()

        # creating windows
        screen = pygame.display.set_mode((800, 600))
        background = pygame.image.load('../images/pixelbackground.jpg')

        # title & icon
        pygame.display.set_caption("Heimdall")

        # Sound
        pygame.mixer.init()
        pygame.mixer.music.load("../sounds/main.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # Vars
        menu, play, shop, stats = True, False, False, False

        # launch bot game
        game = Game()

        # loop game
        running = True
        while running:

            # color front
            screen.blit(background, (0, 0))

            if menu:
                button.logo_heimdall(screen, False)
                button.fight_button(screen, False)
                button.shop_button(screen, False)
                button.stats_button(screen, False)
                button.leave_button(screen, False)

            if shop:
                button.custom_button(screen, False, "Boutique", 72, "#FFFFFF", 310, 20)
                button.back_button(screen, False)

            if play:
                button.back_button(screen, False)

            if stats:
                button.custom_button(screen, False, "Statistiques", 72, "#FFFFFF", 280, 20)
                button.back_button(screen, False)

            # update windows
            pygame.display.flip()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Si on clique sur COMBATTRE
                    if button.fight_button(screen, True).collidepoint(event.pos):
                        menu = False
                        play = True

                    # Si on clique sur BOUTIQUE
                    if button.shop_button(screen, True).collidepoint(event.pos):
                        menu = False
                        shop = True

                    # Si on clique sur STATS
                    if button.stats_button(screen, True).collidepoint(event.pos):
                        menu = False
                        stats = True

                    # Si tu cliques sur retour
                    if button.back_button(screen, True).collidepoint(event.pos):
                        menu = True
                        play, shop, stats = False, False, False

                    # Si on clique sur QUITTER
                    if button.leave_button(screen, True).collidepoint(event.pos):
                        Stop.stop(connexion_with_serveur)
                if event.type == pygame.QUIT:
                    Stop.stop(connexion_with_serveur)

            pygame.display.update()

except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    Stop.stop(connexion_with_serveur)
