#Importing the pygame lib.
import pygame

#Initializing the pygame.
pygame.init()
#Creating the dimensions of the display.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating the display.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Adding a caption.
pygame.display.set_caption("Discrete Movement!")
#Setting a flag.
not_running = False
#The main game loop.
while not not_running:
    #Starting a for loop.
    