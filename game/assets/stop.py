import pygame

def stop(connexion_with_serveur):
    connexion_with_serveur.close()
    pygame.mixer.music.stop()
    running = False
    exit()
