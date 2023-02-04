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
from box import Box
from floor import Floor
from rock import Rock

NUMBER_OF_ROCKS = 5

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
box = Box()
floor = Floor()

rocks = [None] * NUMBER_OF_ROCKS
for i in range(NUMBER_OF_ROCKS):
    rocks[i] = Rock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                box.succ(floor)


    pressed_keys = pygame.key.get_pressed()

    box.update(pressed_keys)

    if floor.allPainted():
        running = False
    
    screen.blit(floor.surf, floor.rect)
    screen.blit(box.surf, box.rect)

    for i in range(NUMBER_OF_ROCKS):
        screen.blit(rocks[i].image, rocks[i].rect)

    pygame.display.flip()
    clock.tick(FRAME_RATE)

pygame.display.quit()
pygame.quit()