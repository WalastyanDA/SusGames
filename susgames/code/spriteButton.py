import pygame

class SpriteButton(pygame.sprite.Sprite):
    def __init__(self, image: pygame.image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        

    def update(self, mouse_pos, mouse_down):
        if mouse_down:
            if self.rect.collidepoint(mouse_pos):
                # Do something when the button is clicked
                return True