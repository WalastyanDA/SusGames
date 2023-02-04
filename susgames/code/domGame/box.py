import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

from constants import *
from helper import getRectInBounds

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super(Box, self).__init__()
        self.surf = pygame.Surface((75, 75))
        #self.surf.fill(CYAN)
        self.rect = self.surf.get_rect()
        self.image = pygame.image.load(
            "./susgames/assets/images/domGame/box.png"
        )
        self.succCooldown = 0

    def update(self, pressed_keys, rocks):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            if self.overlaps(rocks):
                self.rect.move_ip(0, 5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            if self.overlaps(rocks):
                self.rect.move_ip(0, -5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            if self.overlaps(rocks):
                self.rect.move_ip(5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            if self.overlaps(rocks):
                self.rect.move_ip(-5, 0)
            
        self.rect = getRectInBounds(self.rect)
        
        if self.succCooldown > 0:
            self.succCooldown -= 1

    def succ(self, floor):
        if self.succCooldown == 0:
            area = pygame.Rect(
                self.rect.x - ((SUCC_RADIUS - self.rect.width) / 2),
                self.rect.y - ((SUCC_RADIUS - self.rect.height) / 2),
                SUCC_RADIUS,
                SUCC_RADIUS
            )
            area = getRectInBounds(area)

            floor.paintRect(area)
            self.succCooldown = 20

    def overlaps(self, rocks):
        for rock in rocks:
            if pygame.sprite.collide_mask(self, rock):
                return True

        return False

