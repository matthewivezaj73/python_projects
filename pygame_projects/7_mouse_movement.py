#Importing the pygame lib.
import pygame
#Initializing pygame.
pygame.init()

#Creating parameters of the game surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating a display surface.
display_surface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
#Setting a caption.
pygame.display.set_caption("Mouse Movement!")
#Setting a flag.
not_running = False
#Testing for user interaction.
while not not_running:
    for event in pygame.event.get():