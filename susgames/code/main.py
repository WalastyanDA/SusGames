import pygame
import startMenu
import sys

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))


startMenu.show(screen)
