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

from time import time as time

from constants import *
from box import Box
from floor import Floor
from rock import Rock

NUMBER_OF_ROCKS = 5

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
floor = Floor()

rocks = []
while len(rocks) < NUMBER_OF_ROCKS:
    newRock = Rock()

    collide = False
    for rock in rocks:
        if pygame.sprite.collide_mask(rock, newRock):
            collide = True
            break;

    if not collide:
        rocks.append(newRock)

box = None
while box == None:
    newBox = Box()

    collide = False
    for rock in rocks:
        if pygame.sprite.collide_mask(rock, newBox):
            collide = True
            break;

    if not collide:
        box = newBox

startTime = time()
while time() < startTime + CLEANUP_TIME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                box.succ(floor)

    pressed_keys = pygame.key.get_pressed()

    box.update(pressed_keys, rocks)

    screen.blit(floor.surf, floor.rect)

    for i in range(NUMBER_OF_ROCKS):
        screen.blit(rocks[i].image, rocks[i].rect)

    screen.blit(box.image, box.rect)

    pygame.display.flip()
    clock.tick(FRAME_RATE)

print(str(floor.cleaned))

pygame.display.quit()
pygame.quit()