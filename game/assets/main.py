#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame, math, time, datetime, socket
import buttons as button
import credentials as credentials
import stop as Stop
from player import Player
from bot import Bot

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
    lose = data.decode("utf-8")
    data = connexion_with_serveur.recv(1024)
    level = data.decode("utf-8")

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
        menu, play, shop, stats, victory = True, False, False, False, None

        player = Player(int(level), int(wins), int(lose), int(money))
        bot = Bot()

        # loop game
        running = True
        your_turn = True
        while running:

            # color front
            screen.blit(background, (0, 0))

            if menu:
                button.custom_button(screen, False, str(player.money) + " PO", 42, "#FFFFFF", 30, 20)
                button.custom_button(screen, False, "Level " + str(player.level), 42, "#FFFFFF", 650, 20)
                button.custom_button(screen, False, "Online " + str(online), 42, "#FFFFFF", 650, 550)
                button.custom_button(screen, False, "Potions : " + str(player.potions), 42, "#FFFFFF", 20, 550)
                button.logo_heimdall(screen, False)
                button.fight_button(screen, False)
                button.shop_button(screen, False)
                button.stats_button(screen, False)
                button.leave_button(screen, False)

            if shop:
                button.custom_button(screen, False, "Boutique", 72, "#FFFFFF", 300, 20)
                button.custom_button(screen, False, str(player.money) + " PO", 42, "#FFFFFF", 30, 20)
                button.shop_heal_button(screen, False)
                button.custom_button(screen, False, "10 PO", 40, "#FFFFFF", 350, 380)
                button.buy_button(screen, False)
                button.back_button(screen, False)

            if play:
                screen.blit(player.image, player.rect)
                player.update_health_bar(screen)
                bot.update_health_bar(screen)
                screen.blit(bot.image, bot.rect)
                button.back_button(screen, False)
                if your_turn:
                    button.sword_button(screen, False)
                    button.heal_button(screen, False)
                    button.custom_button(screen, False, str(player.potions), 40, "#FFFFFF", 100, 65)
                else:
                    pygame.time.delay(2000)
                    if player.health - bot.damage <= 0:
                        player.health = player.max_health
                        bot.health = bot.max_health
                        player.lose += 1
                        victory = False
                        shop, stats, play = False, False, False
                    else:
                        player.take_damage(bot.attack())
                    your_turn = not your_turn

            if stats:
                button.custom_button(screen, False, "Statistiques", 72, "#FFFFFF", 280, 20)
                button.custom_button(screen, False, str(player.win) + " victoires", 40, "#FFFFFF", 320, 200)
                button.custom_button(screen, False, str(player.lose) + " défaites", 40, "#FFFFFF", 320, 250)
                button.custom_button(screen, False, str(round(player.win / player.lose, 2)) + " de ratio", 40, "#FFFFFF", 320, 300)
                button.custom_button(screen, False, "Level " + str(player.level), 40, "#FFFFFF", 320, 350)
                button.custom_button(screen, False, str(player.money) + " PO", 40, "#FFFFFF", 320, 400)
                button.back_button(screen, False)

            if victory is not None:
                if victory:
                    button.custom_button(screen, False, "Victoire !", 72, "#FFFFFF", 280, 250)
                if not victory:
                    button.custom_button(screen, False, "Défaite !", 72, "#FFFFFF", 280, 250)
                button.back_button(screen, False)

            # update windows
            pygame.display.flip()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Si on clique sur COMBATTRE
                    if button.fight_button(screen, True).collidepoint(event.pos):
                        menu, shop, stats = False, False, False
                        play = True

                    # Si on clique sur BOUTIQUE
                    if button.shop_button(screen, True).collidepoint(event.pos):
                        menu = False
                        shop = True

                    # Si on clique sur STATS
                    if button.stats_button(screen, True).collidepoint(event.pos):
                        menu, shop, play = False, False, False
                        stats = True

                    # Si on clique sur BUY
                    if button.buy_button(screen, True).collidepoint(event.pos):
                        player.spend_money(10)
                        money = player.money
                        menu = True
                        play, shop, stats = False, False, False

                    # Si on clique sur SWORD
                    if button.sword_button(screen, True).collidepoint(event.pos):
                        if your_turn:
                            if bot.health - player.damage <= 0:
                                player.health = player.max_health
                                bot.health = bot.max_health
                                player.money += 15
                                player.win += 1
                                victory = True
                                shop, stats, play = False, False, False
                            else:
                                bot.take_damage(player.attack())
                                bot.update_health_bar(screen)
                            your_turn = not your_turn

                    # Si tu cliques sur HEAL
                    if button.heal_button(screen, True).collidepoint(event.pos):
                        if your_turn:
                            if player.potions > 0:
                                player.potions -= 1
                                player.health += player.heal
                                player.update_health_bar(screen)
                            else:
                                print("Pas assez de potions, allez en acheter après le combat")
                            your_turn = not your_turn

                    # Si tu cliques sur retour
                    if button.back_button(screen, True).collidepoint(event.pos):
                        if play:
                            player.lose += 1
                            player.health = player.max_health
                            bot.health = bot.max_health
                            victory = False
                            menu, play, shop, stats = False, False, False, False
                        else:
                            victory = None
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
