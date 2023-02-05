import pygame
import random
import time

class RubbishItem:
    def __init__(self, size: int, x: int, y):
        self.category = random.choice(
            ["Metal", "Paper", "Glass", "Plastic", "Unrecyclable"])
        self.size = size
        self.x = x
        self.y = y
    def get_color(self):
        colors = {
            "Metal":(255, 0, 0), 
            "Paper": (255, 255, 0), 
            "Glass": (0, 255, 0), 
            "Plastic": (0, 0, 255),
            "Unrecyclable": (0,0,0)
            }
        return colors[self.category]

class ConveyorGame:
    def __init__(self, screen: pygame.Surface):
        self.handleEvents
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.bin_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
        self.conveyor_speed = 5
        self.object_speed = 5
        self.objects = [] 
        self.object_radius = 10
        
        self.conveyor_x = self.screen_width * 0.1
        self.conveyor_y = self.screen_height * 0.5
        self.conveyor_width = self.screen_width * 0.8
        self.conveyor_height = self.screen_height * 0.1
        self.add_object()


    def add_object(self):
        y = random.randint(self.conveyor_x, self.conveyor_x + self.conveyor_height) + 0.5*self.screen_height - 0.5*self.conveyor_height
        x = self.screen_width * 0.1
        size = random.randint(10,30)
        new_item = RubbishItem(size, x, y)
        self.objects.append(new_item) # , size
        print("Spawned Object")
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        #print("w: ", self.screen_height, "h: ", self.screen_height)
        self.conveyor_width = self.screen_width * 0.8
        self.conveyor_height = self.screen_height * 0.2
        self.conveyor_x = self.screen_width * 0.1
        self.conveyor_y = self.screen_height * 0.5
        print(self.conveyor_y)

        rectangle = pygame.Rect(10,300,10,10)
        pygame.draw.rect(self.screen, (255,0,0),rectangle)

        # Draw the conveyor
        conveyor_rect = pygame.Rect(self.conveyor_x, self.conveyor_y, self.conveyor_width, self.conveyor_height)
        for i in range(0, self.screen_width, int(self.conveyor_width/len(self.bin_colors))):
            conveyor_rect.left = self.conveyor_x + i
            pygame.draw.rect(self.screen, (128, 128, 128), conveyor_rect)

        # Draw the bins
        bin_height = self.screen_height * 0.2
        bin_width = bin_height
        bin_labels = ["Metals", "Paper", "Glass", "Plastics"]
        for i, color in enumerate(self.bin_colors):
            if color == (255, 0, 0) or color == (255, 255, 0):
                bin_x = ((self.screen_width/3)*2) - bin_height/2
                #print("binx: ",bin_x)
            else:
                bin_x = ((self.screen_width/3)*1) - bin_height/2
            if color == (255, 0, 0) or color == (0, 255, 0):
                bin_y = ((self.screen_width/3)*2) - bin_height
            else:
                bin_y = ((self.screen_width/3)*1)- bin_height
            pygame.draw.rect(self.screen, color, (bin_x, bin_y, bin_width, bin_height))

            font = pygame.font.Font(None, 30)
            text = font.render(bin_labels[i], True, (255, 255, 255))
            text_rect = text.get_rect(center=(bin_x + bin_width / 2, bin_y + bin_height / 2))
            self.screen.blit(text, text_rect)
        
        # Move the objects

        for i, item in enumerate(self.objects):
            item.x += self.conveyor_speed
            if item.x > self.screen_width or item.y < 0:
                self.objects.pop(i)


        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > 500: # 1000ms = 1s
            self.add_object()
            self.spawn_time = current_time

        # Draw the objects
        for item in self.objects:

            pygame.draw.circle(self.screen, item.get_color(), (item.x, item.y), item.size)




    def itemBinned(self, itemType, bin):
        # This function is called when an object is dropped in a bin.
        # It updates the object's position to the top of the selected bin.

        bin_width = self.screen_width * 0.1
        bin_height = self.screen_height * 0.8
        bin_x = self.screen_width * 0.1 - bin_width - 10
        bin_y = self.screen_height * 0.1 + bin * (bin_height + 10)
        font = pygame.font.Font(None, 30)
        text = font.render(itemType, True, (255, 255, 255))
        text_rect = text.get_rect(center=(bin_x + bin_width / 2, bin_y + bin_height / 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # handle mouse click events to pick up objects and place them in bins
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, (x, y, category) in enumerate(self.objects):
                    # check if the mouse is over the object
                    if x < mouse_x < x + self.object_width and y - self.object_height / 2 < mouse_y < y + self.object_height / 2:
                        self.itemBinned(category, self.getBinForCoordinates(mouse_x, mouse_y))
                        del self.objects[i]
                        break


    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.handleEvents()
            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
