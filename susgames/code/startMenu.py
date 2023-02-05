import pygame
import os
import gamesList
import spriteButton
from utils import ASSETS_PATH, IMAGE_PATH, FONTS_PATH, quitGame

# Main menu
def show(screen: pygame.surface):
    """Shows the main menu on the pygame surface"""

    # the scene's sprite group
    spriteGroup = pygame.sprite.Group()
    
    bg = pygame.image.load(os.path.join(IMAGE_PATH, "startBackground.png"))
    
    # Load font for menu buttons
    font = pygame.font.Font(os.path.join(FONTS_PATH, "KenneyBold.ttf"), 30)

    # Define menu buttons
    play_button = font.render("Play", True, (255, 255, 255))
    quit_button = font.render("Quit", True, (255, 255, 255))

    # Set button rects
    play_rect = play_button.get_rect(center=(400, 200))
    quit_rect = quit_button.get_rect(center=(400, 300))

    #########################
    # settings button stuff #
    #########################

    gear_img = pygame.image.load(os.path.join(IMAGE_PATH, "gear.png"))

    # Settings button circle
    screenWidth, screenHeight = pygame.display.get_surface().get_size()
    settings_radius = gear_img.get_width()/2
    settings_coords = (screenWidth - settings_radius, settings_radius)

    settings_button = spriteButton.SpriteButton(gear_img, settings_coords)
    spriteGroup.add(settings_button)

    running = True
    while running:
        # Clear screen
        screen.blit(bg, (0,0))
        # Draw buttons
        screen.blit(play_button, play_rect)
        screen.blit(quit_button, quit_rect)

        # Draw settings button circle
        spriteGroup.draw(screen)

        # Update screen
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quitGame()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check if buttons were clicked
                mouse_pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    # Context switch to gamesList.py
                    gamesList.show(screen)
                elif quit_rect.collidepoint(mouse_pos):
                    running = False
                elif (settings_coords[0] - mouse_pos[0])**2 + \
                    (settings_coords[1]- mouse_pos[1])**2 < settings_radius**2:
                    # Open settings menu
                    # TODO: Add code to open settings menu
                    print("test")
                
    quitGame()


