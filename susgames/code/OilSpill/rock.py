import pygame
from random import randint

from OilSpill.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROCK_SIZE

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.image = pygame.image.load(
            "./susgames/assets/images/OilSpill/rock.png"
        )
        x = randint(0, SCREEN_WIDTH - ROCK_SIZE)
        y = randint(0, SCREEN_HEIGHT - ROCK_SIZE)
        self.rect = pygame.Rect((x, y), (ROCK_SIZE, ROCK_SIZE))