#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('../images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 0