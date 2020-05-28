#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.font.init()

# player class
class Player(pygame.sprite.Sprite):

    def __init__(self, level, win, lose, money):
        super().__init__()
        self.max_health = 100
        self.health = self.max_health
        self.damage = 50
        self.level = level
        self.win = win
        self.lose = lose
        self.money = money
        self.heal = 35
        self.potions = 0
        self.image = pygame.image.load('../images/player.png')
        self.image = pygame.transform.scale(self.image, (300, 345))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 250

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        bar_position = [self.rect.x + 12, self.rect.y - 20, self.health, 5]

        background_bar_color = (255, 0, 0)
        background_bar_position = [self.rect.x + 12, self.rect.y - 20, self.max_health, 5]

        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def heal(self):
        self.health += self.heal

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def attack(self):
        return self.damage

    def add_potions(self, amount):
        self.potions += amount

    def spend_money(self, money_amount):
        if self.money - money_amount >= 0:
            self.money -= money_amount
            self.add_potions(1)
        else:
            print("Pas assez de PO")

    def win(self):
        self.win += 1

    def lose(self):
        self.lose += 1
