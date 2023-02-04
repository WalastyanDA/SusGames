import pygame

from constants import *

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surf.fill((BLACK))
        self.rect = self.surf.get_rect()