#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# game class
class Game:

    def __init__(self):
        self.player = Player()
        self.bot = Bot()

# player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('game/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 0

class Bot(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('game/images/bluekappa.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 350

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