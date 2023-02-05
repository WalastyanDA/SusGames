import pygame
import os
from random import randint

from OilSpill.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROCK_SIZE, OIL_IMAGE_PATH

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.image = pygame.image.load(
            os.path.join(OIL_IMAGE_PATH, "rock.png")
        )
        x = randint(0, SCREEN_WIDTH - ROCK_SIZE)
        y = randint(0, SCREEN_HEIGHT - ROCK_SIZE)
        self.rect = pygame.Rect((x, y), (ROCK_SIZE, ROCK_SIZE))