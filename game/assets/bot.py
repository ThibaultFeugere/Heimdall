#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# player class
class Bot(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.damage = 10
        self.image = pygame.image.load('../images/bot.png')
        self.image = pygame.transform.scale(self.image, (250, 280))
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 250

    def heal(self, heal_amount):
        self.health += heal_amount

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def attack(self):
        return self.damage
