#Importing pygame.
import pygame
#Initialize pygame.
pygame.init()
#Create a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#The main game loop.
not_running = False
#Testing for reaction.
while not not_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            not_running = True