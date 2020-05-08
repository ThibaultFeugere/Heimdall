#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame as pg
import pygame_textinput
import os.path


pg.font.init()

# path file
filepath = os.path.dirname(__file__)

# creating windows
screen = pg.display.set_mode((800,600))

# title & icone
pg.display.set_caption("Heimdall")
#icon = pg.image.load(filepath,'images/heimdall.png').convert()
#pg.display.set_icon(icon)

# text input/object
textinput = pygame_textinput.TextInput()

# loop game
while True:

    # color front
    screen.fill((255,255,255))

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()
       
    textinput.update(pg.event.get())
    screen.blit(textinput.get_surface(), (10,10))

    if textinput.update(events):
        print(textinput.get_text())

    pg.display.update()
