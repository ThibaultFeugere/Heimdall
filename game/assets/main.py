#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame, math, time, datetime, socket
from game import Game
import buttons.buttons as button
import credentials as credentials
import stop as Stop

adresse, port = ("127.0.0.1", 5555)
Login = None

# Socket donnant l'accès au serveur
connexion_with_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_with_serveur.connect((adresse, port))

    Login = credentials.ask(connexion_with_serveur, Stop)

    data = connexion_with_serveur.recv(1024)
    online = data.decode("utf-8")
    data = connexion_with_serveur.recv(1024)
    money = data.decode("utf-8")
    data = connexion_with_serveur.recv(1024)
    wins = data.decode("utf-8")
    data = connexion_with_serveur.recv(1024)
    loses = data.decode("utf-8")
    data = connexion_with_serveur.recv(1024)
    level = data.decode("utf-8")
    ratio = str(int(wins) / int(loses))

    if Login == True:
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
                button.custom_button(screen, False, money + " PO", 42, "#FFFFFF", 30, 20)
                button.custom_button(screen, False, "Level " + level, 42, "#FFFFFF", 650, 20)
                button.custom_button(screen, False, "Online " + online, 42, "#FFFFFF", 650, 500)
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
                button.custom_button(screen, False, wins + " victoires", 40, "#FFFFFF", 320, 200)
                button.custom_button(screen, False, loses + " défaites", 40, "#FFFFFF", 320, 250)
                button.custom_button(screen, False, ratio + " de ratio", 40, "#FFFFFF", 320, 300)
                button.custom_button(screen, False, "Level " + level, 40, "#FFFFFF", 320, 350)
                button.custom_button(screen, False, money + " PO", 40, "#FFFFFF", 320, 400)
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
                        Stop.stop(connexion_with_serveur, True)
                if event.type == pygame.QUIT:
                    Stop.stop(connexion_with_serveur, True)

            pygame.display.update()

except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    Stop.stop(connexion_with_serveur, False)
