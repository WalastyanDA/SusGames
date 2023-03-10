import pygame

from pygame.locals import (
    K_SPACE,
)

from time import time, sleep

import startMenu
from utils import *
from OilSpill.constants import *
from OilSpill.boat import Boat
from OilSpill.sea import Sea
from OilSpill.oil import Oil
from OilSpill.rock import Rock


def show(screen: pygame.surface):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE)

    pygame.display.set_caption("Oil Spill")

    boat = Boat()

    sea = Sea()

    oils = []
    while len(oils) < NUMBER_OF_OILS:
        newOil = Oil()
        collide = False

        for oil in oils:
            if pygame.sprite.collide_mask(oil, newOil):
                collide = True
                break;

        if pygame.sprite.collide_mask(boat, newOil):
            collide = True

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

        for oil in oils:
            if pygame.sprite.collide_mask(oil, newRock):
                collide = True
                break

        if pygame.sprite.collide_mask(boat, newOil):
            collide = True

        if not collide:
            rocks.append(newRock)

    startTime = time()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_SPACE]:
                    boat.suck(oils)

        pressed_keys = pygame.key.get_pressed()
        boat.update(pressed_keys, rocks)

        screen.blit(sea.image, sea.rect)

        for i in range(NUMBER_OF_OILS - boat.sucked):
            screen.blit(oils[i].image, oils[i].rect)

        for i in range(NUMBER_OF_ROCKS):
            screen.blit(rocks[i].image, rocks[i].rect)

        screen.blit(boat.image, boat.rect)

        timer = font.render(
            str(round(time() - startTime, 1)),
            True,
            WHITE
        )
        screen.blit(timer, (0, 0))

        pygame.display.flip()
        clock.tick(FRAME_RATE)

        if boat.sucked == NUMBER_OF_OILS or (time() - startTime) > CLEANUP_TIME:
            loop = False

    endTime = time()

    endText = ""
    if endTime - startTime >= CLEANUP_TIME:
        endText = "You failed to clean up in time!"
    else:
        endText = "You cleaned up in " + str(round((endTime - startTime), 1)) + " seconds!"

    screen.blit(sea.image, sea.rect)
    score = font.render(
        endText,
        True,
        WHITE
    )
    scoreWidthHalf = score.get_rect().width / 2
    scoreHeightHalf = score.get_rect().height / 2
    screen.blit(
        score, 
        (SCREEN_WIDTH / 2 - scoreWidthHalf, SCREEN_HEIGHT / 2 - scoreHeightHalf)
    )
    pygame.display.flip()
    sleep(5)

    startMenu.show(screen)
    
