import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, mouse_pos, mouse_down):
        if mouse_down:
            if self.rect.collidepoint(mouse_pos):
                # Do something when the button is clicked
                pass