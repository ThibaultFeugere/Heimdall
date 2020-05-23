#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# bot class
class Bot(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('../images/bluekappa.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 350
