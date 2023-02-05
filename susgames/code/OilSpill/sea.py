import pygame
import os

from OilSpill.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OIL_IMAGE_PATH

class Sea(pygame.sprite.Sprite):
    def __init__(self):
        super(Sea, self).__init__()
        self.image = pygame.image.load(
            os.path.join(OIL_IMAGE_PATH, "sea.png")
        )
        self.rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))