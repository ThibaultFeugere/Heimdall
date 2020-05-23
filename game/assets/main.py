#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame, math, time, datetime, socket
from game import Game

adresse, port = ("127.0.0.1", 5555)

# Socket donnant l'accès au serveur
connexion_with_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Demande de connexion au serveur
    connexion_with_serveur.connect((adresse, port))

    # Connexion
    username = input("Quel est votre pseudo ?\n")
    password = input("Quel est votre mot de passe ?\n")
    connexion_with_serveur.sendall(("username," + username).encode("utf8"))
    connexion_with_serveur.sendall(("password," + password).encode("utf8"))

    pygame.init()
    pygame.font.init()

    # creating windows
    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('../images/pixelbackground.jpg')

    # timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)

    # title & icon
    pygame.display.set_caption("Heimdall")

    # Sound
    pygame.mixer.init()
    pygame.mixer.music.load("../sounds/main.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    # Vars
    menu, play, shop, stats = True, False, False, False

    # Logo
    logo = pygame.image.load('../images/logo.png')
    logo_rect = logo.get_rect()
    logo_rect.x = 0
    logo_rect.y = 0

    # Buttons
    ## Combattre
    play_button = pygame.image.load('../images/combattre.png')
    play_button = pygame.transform.scale(play_button, (200, 50))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 2.65)
    play_button_rect.y = 200

    ## Shop
    shop_button = pygame.image.load('../images/boutique.png')
    shop_button = pygame.transform.scale(shop_button, (200, 50))
    shop_button_rect = shop_button.get_rect()
    shop_button_rect.x = math.ceil(screen.get_width() / 2.65)
    shop_button_rect.y = 270

    ## Statistiques
    stats_button = pygame.image.load('../images/stats.png')
    stats_button = pygame.transform.scale(stats_button, (200, 50))
    stats_button_rect = shop_button.get_rect()
    stats_button_rect.x = math.ceil(screen.get_width() / 2.65)
    stats_button_rect.y = 340

    ## Deconnexion
    leave_button = pygame.image.load('../images/quitter.png')
    leave_button = pygame.transform.scale(leave_button, (200, 50))
    leave_button_rect = leave_button.get_rect()
    leave_button_rect.x = math.ceil(screen.get_width() / 2.65)
    leave_button_rect.y = 410

    # launch bot game
    game = Game()

    # loop game
    running = True
    while running:

        # color front
        screen.blit(background, (0, 0))

        if menu:
            screen.blit(logo, logo_rect)
            screen.blit(play_button, play_button_rect)
            screen.blit(shop_button, shop_button_rect)
            screen.blit(stats_button, stats_button_rect)
            screen.blit(leave_button, leave_button_rect)

        if shop:
            police = pygame.font.Font(None, 72)
            title = police.render("Boutique", True, pygame.Color("#FFFFFF"))
            title_rect = title.get_rect()
            title_rect.x = math.ceil(screen.get_width() / 2.8)
            title_rect.y = 30
            screen.blit(title, title_rect)
        if play:
            # if datetime.datetime.utcnow() > timer_stop:
            #  menu = True
            #  play = False
            pass

        if stats:
            police = pygame.font.Font(None, 72)
            title = police.render("Statistiques", True, pygame.Color("#FFFFFF"))
            title_rect = title.get_rect()
            title_rect.x = math.ceil(screen.get_width() / 3)
            title_rect.y = 30
            screen.blit(title, title_rect)

        # update windows
        pygame.display.flip()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si on clique sur COMBATTRE
                if play_button_rect.collidepoint(event.pos):
                    menu = False
                    play = True

                # Si on clique sur BOUTIQUE
                if shop_button_rect.collidepoint(event.pos):
                    menu = False
                    shop = True

                # Si on clique sur STATS
                if stats_button_rect.collidepoint(event.pos):
                    menu = False
                    stats = True

                # Si on clique sur QUITTER
                if leave_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    menu = False
                    running = False
                    exit()
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
                exit()

        pygame.display.update()

except ConnectionRefusedError:
    print("Connexion au serveur échouée")
finally:
    # On ferme la connexion
    connexion_with_serveur.close()
