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

from time import time, sleep

from constants import *
from boat import Boat
from floor import Floor
from oil import Oil
from rock import Rock

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oil Spill")

floor = Floor()

oils = []
while len(oils) < NUMBER_OF_OILS:
    newOil = Oil()

    collide = False
    for oil in oils:
        if pygame.sprite.collide_mask(oil, newOil):
            collide = True
            break;

    if not collide:
        oils.append(newOil)

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

boat = None
while boat == None:
    newBoat = Boat()

    collide = False
    for rock in rocks:
        if pygame.sprite.collide_mask(rock, newBoat):
            collide = True
            break;

    if not collide:
        boat = newBoat

startTime = time()
while time() < startTime + CLEANUP_TIME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                boat.succ(oils)

    pressed_keys = pygame.key.get_pressed()

    boat.update(pressed_keys, rocks)

    screen.blit(floor.image, floor.rect)

    for i in range(NUMBER_OF_OILS - boat.succed):
        screen.blit(oils[i].image, oils[i].rect)

    for i in range(NUMBER_OF_ROCKS):
        screen.blit(rocks[i].image, rocks[i].rect)

    screen.blit(boat.image, boat.rect)

    timer = font.render(
        str(round((CLEANUP_TIME - (time() - startTime)), 1)),
        True,
        WHITE
    )
    screen.blit(timer, (0, 0))

    pygame.display.flip()
    clock.tick(FRAME_RATE)

screen.blit(floor.image, floor.rect)
score = font.render(
    str(boat.succed),
    True,
    WHITE
)
screen.blit(score, (0, 0))
pygame.display.flip()
sleep(10)

print(str(boat.succed))

pygame.display.quit()
pygame.quit()