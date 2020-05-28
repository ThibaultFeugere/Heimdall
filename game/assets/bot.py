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
        self.damage = 20
        self.image = pygame.image.load('../images/bot.png')
        self.image = pygame.transform.scale(self.image, (250, 280))
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 250

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        bar_position = [self.rect.x + 12, self.rect.y - 20, self.health, 5]

        background_bar_color = (255, 0, 0)
        background_bar_position = [self.rect.x + 12, self.rect.y - 20, self.max_health, 5]

        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def heal(self, heal_amount):
        self.health += heal_amount

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def attack(self):
        return self.damage
