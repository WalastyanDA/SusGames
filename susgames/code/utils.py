import pathlib
import os
import pygame

ASSETS_PATH = os.path.join("susgames","assets")
IMAGE_PATH = os.path.join(ASSETS_PATH, "images")
FONTS_PATH = os.path.join(ASSETS_PATH, "fonts")

def quitGame():
    pygame.display.quit()
    pygame.quit()
    exit()