#Importing the library.
import pygame

#Initialize pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating a display surface.
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
#Creating a caption.
pygame.display.set_caption("Adding Sounds!")
#Setting a flag.
not_done = False
#Testing for the user to quit the game..