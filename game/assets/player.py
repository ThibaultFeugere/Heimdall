#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.damage = 10
        self.level = 13
        self.win = 10
        self.lose = 12
        self.money = 100
        self.image = pygame.image.load('../images/player.png')
        self.image = pygame.transform.scale(self.image, (300, 345))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 250

    def heal(self, heal_amount):
        self.health += heal_amount

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def attack(self):
        return self.damage

    def spend_money(self, money_amount):
        self.money -= money_amount

    def win(self):
        self.win += 1

    def lose(self):
        self.lose += 1
