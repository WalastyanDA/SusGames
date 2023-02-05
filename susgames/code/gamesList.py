import pygame
import startMenu
import conveyorGame
import os
from utils import ASSETS_PATH, IMAGE_PATH, FONTS_PATH, quitGame
#import domGame.domGame as domGame

def show(screen: pygame.surface):
    # load background image
    bg = pygame.image.load(os.path.join(IMAGE_PATH, "startBackground.png"))
    
    # Load font for menu buttons
    font = pygame.font.Font(os.path.join(FONTS_PATH, "KenneyBold.ttf"), 30)

    # Define menu buttons
    back_button = font.render("Back", True, (255, 255, 255))
    game_buttons = [font.render("domGame", True, (255, 255, 255)),
                    font.render("Conveyor Game", True, (255, 255, 255)),
                    font.render("Minigame 3", True, (255, 255, 255))]
    game_rects = [button.get_rect(center=(400, 200 + 100 * i)) for i, button in enumerate(game_buttons)]

    # Settings button circle
    settings_radius = 20
    settings_x = 780
    settings_y = 20

    # Set back button rect
    back_rect = back_button.get_rect(topleft=(20, 20))

    # Main loop
    running = True
    while running:
        # Clear screen
        screen.blit(bg, (0,0))
        
        # Draw buttons
        screen.blit(back_button, back_rect)
        for button, rect in zip(game_buttons, game_rects):
            screen.blit(button, rect)
        
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
                if back_rect.collidepoint(mouse_pos):
                    # Go back to main menu
                    startMenu.show(screen)
                
                
                for minigame, rect in enumerate(game_rects):
                    if rect.collidepoint(mouse_pos):
                        # Start a minigame
                        # TODO: Add code to start a minigame

                        # replace the passes with the code to start the corresponding game
                        match minigame:
                            case 0:
                                pass
                            case 1:
                                game = conveyorGame.ConveyorGame(screen)
                                game.start()
                            case 2:
                                pass
                    
        

