import pygame

from constants import *

BASE_COLOUR = TRANSPARENT
COVER_COLOUR = BLACK


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.image = pygame.image.load(
            "./susgames/assets/images/OilSpill/sea.png"
        )
        self.rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))