import pygame
import os


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

from OilSpill.constants import *
from OilSpill.helper import getRectInBounds

class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super(Boat, self).__init__()
        self.image = pygame.image.load(
            os.path.join(OIL_IMAGE_PATH, "boat.png")
        )
        self.baseImage = self.image.copy()
        self.rect = pygame.Rect((0, 0), (BOAT_SIZE, BOAT_SIZE))
        self.suckCooldown = 0
        self.sucked = 0

    def update(self, pressed_keys, rocks):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.image = self.baseImage
            if self.overlaps(rocks):
                self.rect.move_ip(0, 5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.image = pygame.transform.rotate(self.baseImage, 180)
            if self.overlaps(rocks):
                self.rect.move_ip(0, -5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.image = pygame.transform.rotate(self.baseImage, 90)
            if self.overlaps(rocks):
                self.rect.move_ip(5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.image = pygame.transform.rotate(self.baseImage, -90)
            if self.overlaps(rocks):
                self.rect.move_ip(-5, 0)
            
        self.rect = getRectInBounds(self.rect)
        
        if self.suckCooldown > 0:
            self.suckCooldown -= 1

    def suck(self, oils):
        if self.suckCooldown == 0:
            for oil in oils:
                if pygame.sprite.collide_mask(self, oil):
                    oils.remove(oil)
                    self.sucked += 1
                    break

            self.suckCooldown = SUCK_COOLDOWN

    def overlaps(self, rocks):
        for rock in rocks:
            if pygame.sprite.collide_mask(self, rock):
                return True

        return False