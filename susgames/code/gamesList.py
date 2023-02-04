import pygame

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load font for menu buttons
font = pygame.font.Font(None, 30)

# Define menu buttons
back_button = font.render("Back", True, (255, 255, 255))
game_buttons = [font.render("Minigame 1", True, (255, 255, 255)),
                font.render("Minigame 2", True, (255, 255, 255)),
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
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if buttons were clicked
            mouse_pos = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_pos):
                # Go back to main menu
                # TODO: Add code to go back to main menu
                pass
            for rect in game_rects:
                if rect.collidepoint(mouse_pos):
                    # Start a minigame
                    # TODO: Add code to start a minigame
                    pass
            if (settings_x - mouse_pos[0])**2 + (settings_y - mouse_pos[1])**2 < settings_radius**2:
                # Open settings menu
                # TODO: Add code to open settings menu
                pass
                
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw buttons
    screen.blit(back_button, back_rect)
    for button, rect in zip(game_buttons, game_rects):
        screen.blit(button, rect)
    
    # Draw settings button circle
    pygame.draw.circle(screen, (255, 255, 255), (settings_x, settings_y), settings_radius)
    
    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
