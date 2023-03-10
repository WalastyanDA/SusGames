import pygame
from random import randint
import os

from OilSpill.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OIL_WIDTH, OIL_HEIGHT, OIL_IMAGE_PATH

class Oil(pygame.sprite.Sprite):
    def __init__(self):
        super(Oil, self).__init__()
        self.image = pygame.image.load(
            os.path.join(OIL_IMAGE_PATH, "oil.png")
        )
        x = randint(0, SCREEN_WIDTH - OIL_WIDTH)
        y = randint(0, SCREEN_HEIGHT - OIL_HEIGHT)
        self.rect = pygame.Rect((x, y), (OIL_WIDTH, OIL_HEIGHT))