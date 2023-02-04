import pygame

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load font for menu buttons
font = pygame.font.Font(None, 30)

# Define menu buttons
play_button = font.render("Play", True, (255, 255, 255))
quit_button = font.render("Quit", True, (255, 255, 255))

# Set button rects
play_rect = play_button.get_rect(center=(400, 200))
quit_rect = quit_button.get_rect(center=(400, 300))

# Settings button circle
settings_radius = 20
settings_x = 780
settings_y = 20

# Main loop
def run(screen):
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check if buttons were clicked
                mouse_pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    # Context switch to gamesList.py
                    import gamesList
                    gamesList.run(screen)
                elif quit_rect.collidepoint(mouse_pos):
                    running = False
                elif (settings_x - mouse_pos[0])**2 + (settings_y - mouse_pos[1])**2 < settings_radius**2:
                    # Open settings menu
                    # TODO: Add code to open settings menu
                    pass
                
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Draw buttons
        screen.blit(play_button, play_rect)
        screen.blit(quit_button, quit_rect)

        # Draw settings button circle
        pygame.draw.circle(screen, (255, 255, 255), (settings_x, settings_y), settings_radius)

        # Update screen
        pygame.display.update()

# Quit pygame
pygame.quit()
