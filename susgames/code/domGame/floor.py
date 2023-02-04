import pygame

from constants import *

BASE_COLOUR = WHITE
COVER_COLOUR = BLACK


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.surf.fill(COVER_COLOUR)
        self.rect = self.surf.get_rect()
        self.covered = SCREEN_WIDTH * SCREEN_HEIGHT

    def paintRect(self, rect):
        for x in range (rect.left, rect.right):
            for y in range(rect.top, rect.bottom):
                if self.surf.get_at((x, y)) == COVER_COLOUR:
                    self.surf.set_at((x, y), BASE_COLOUR)
                    self.covered -= 1

    def allPainted(self):
        if self.covered > 0:
            return False
        
        else:
            return True