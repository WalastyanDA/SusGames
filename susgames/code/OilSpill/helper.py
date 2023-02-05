from constants import *

def getRectInBounds(rect):
    if rect.left < 0:
        rect.left = 0
    if rect.right > SCREEN_WIDTH:
        rect.right = SCREEN_WIDTH; 
    if rect.top <= 0:
        rect.top = 0
    if rect.bottom >= SCREEN_HEIGHT:
        rect.bottom = SCREEN_HEIGHT
    
    return rect