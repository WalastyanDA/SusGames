import pygame

from OilSpill.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Sea(pygame.sprite.Sprite):
    def __init__(self):
        super(Sea, self).__init__()
        self.image = pygame.image.load(
            "./susgames/assets/images/OilSpill/sea.png"
        )
        self.rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))