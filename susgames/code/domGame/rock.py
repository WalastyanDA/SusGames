import pygame
from random import randint

from constants import *

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.surf = pygame.Surface((80, 80))
        self.surf.fill(GREY)
        self.rect = self.surf.get_rect()
        self.image = pygame.image.load(
            "./susgames/assets/images/domGame/rock.png"
        )
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = randint(0, SCREEN_HEIGHT - self.rect.height)
         