import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from constants import *
from box import Box
from floor import Floor

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
box = Box()
floor = Floor()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()

    box.update(pressed_keys)

    for x in range (box.rect.left, box.rect.right):
        for y in range(box.rect.top, box.rect.bottom):
            floor.surf.set_at((x, y), WHITE)

    screen.fill((255, 255, 255))

    screen.blit(floor.surf, floor.rect)
    screen.blit(box.surf, box.rect)

    pygame.display.flip()
    clock.tick(FRAME_RATE)

pygame.display.quit()
pygame.quit()