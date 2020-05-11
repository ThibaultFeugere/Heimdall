#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from game import Game

pygame.font.init()

# creating windows
screen = pygame.display.set_mode((800,600))
background = pygame.image.load('game/images/pixelbackground.jpg')

# title & icone
pygame.display.set_caption("Heimdall")

# launch bot game
game = Game()

# loop game
running = True
while running:

    # color front
    screen.blit(background, (0, 0))

    # show player
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.bot.image, game.bot.rect)

    # update windows
    pygame.display.flip()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("Stoping launcher")
            running = False
            exit()

    pygame.display.update()