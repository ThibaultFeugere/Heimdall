import pygame, math

# Logo
def logo_heimdall(screen, rect):
    logo = pygame.image.load('../images/logo.png')
    logo_rect = logo.get_rect()
    logo_rect.x = math.ceil(screen.get_width() / 2.65)
    logo_rect.y = 0
    if rect == True:
        return logo_rect
    else:
        screen.blit(logo, logo_rect)

# Buttons
## Combattre
def fight_button(screen, rect):
    fight_button = pygame.image.load('../images/combattre.png')
    fight_button = pygame.transform.scale(fight_button, (200, 50))
    fight_button_rect = fight_button.get_rect()
    fight_button_rect.x = math.ceil(screen.get_width() / 2.65)
    fight_button_rect.y = 200
    if rect == True:
        return fight_button_rect
    else:
        screen.blit(fight_button, fight_button_rect)

## Shop
def shop_button(screen, rect):
    shop_button = pygame.image.load('../images/boutique.png')
    shop_button = pygame.transform.scale(shop_button, (200, 50))
    shop_button_rect = shop_button.get_rect()
    shop_button_rect.x = math.ceil(screen.get_width() / 2.65)
    shop_button_rect.y = 270
    if rect == True:
        return shop_button_rect
    else:
        screen.blit(shop_button, shop_button_rect)

## Statistiques
def stats_button(screen, rect):
    stats_button = pygame.image.load('../images/stats.png')
    stats_button = pygame.transform.scale(stats_button, (200, 50))
    stats_button_rect = stats_button.get_rect()
    stats_button_rect.x = math.ceil(screen.get_width() / 2.65)
    stats_button_rect.y = 340
    if rect == True:
        return stats_button_rect
    else:
        screen.blit(stats_button, stats_button_rect)

## Deconnexion
def leave_button(screen, rect):
    leave_button = pygame.image.load('../images/quitter.png')
    leave_button = pygame.transform.scale(leave_button, (200, 50))
    leave_button_rect = leave_button.get_rect()
    leave_button_rect.x = math.ceil(screen.get_width() / 2.65)
    leave_button_rect.y = 410
    if rect == True:
        return leave_button_rect
    else:
        screen.blit(leave_button, leave_button_rect)

## Retour
def back_button(screen, rect):
    back_button = pygame.image.load('../images/retour.png')
    back_button = pygame.transform.scale(back_button, (200, 50))
    back_button_rect = back_button.get_rect()
    back_button_rect.x = 0
    back_button_rect.y = math.ceil(screen.get_height() - 50)
    if rect == True:
        return back_button_rect
    else:
        screen.blit(back_button, back_button_rect)

## Heal
def heal_button(screen, rect):
    heal_button = pygame.image.load('../images/heal.png')
    heal_button = pygame.transform.scale(heal_button, (159, 205))
    heal_button_rect = heal_button.get_rect()
    heal_button_rect.x = 320
    heal_button_rect.y = 200
    if rect == True:
        return heal_button_rect
    else:
        screen.blit(heal_button, heal_button_rect)

def buy_button(screen, rect):
    buy_button = pygame.image.load('../images/buy.png')
    buy_button = pygame.transform.scale(buy_button, (196, 65))
    buy_button_rect = buy_button.get_rect()
    buy_button_rect.x = 310
    buy_button_rect.y = 350
    if rect == True:
        return buy_button_rect
    else:
        screen.blit(buy_button, buy_button_rect)

def custom_button(screen, rect, text, size, color, x, y):
    police = pygame.font.Font(None, size)
    custom_button = police.render(text, True, pygame.Color(color))
    custom_button_rect = custom_button.get_rect()
    custom_button_rect.x = x
    custom_button_rect.y = y
    if rect == True:
        return custom_button_rect
    else:
        screen.blit(custom_button, custom_button_rect)