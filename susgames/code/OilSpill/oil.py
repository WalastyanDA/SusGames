import pygame
from random import randint

from constants import *

class Oil(pygame.sprite.Sprite):
    def __init__(self):
        super(Oil, self).__init__()
        self.image = pygame.image.load(
            "./susgames/assets/images/OilSpill/oil.png"
        )
        x = randint(0, SCREEN_WIDTH - ROCK_SIZE)
        y = randint(0, SCREEN_HEIGHT - ROCK_SIZE)
        self.rect = pygame.Rect((x, y), (ROCK_SIZE, ROCK_SIZE))