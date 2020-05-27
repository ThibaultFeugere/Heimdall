import pygame

def stop(connexion_with_serveur, music):
    connexion_with_serveur.close()
    if music:
        pygame.mixer.music.stop()
    running = False
    exit()
