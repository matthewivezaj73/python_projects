#Importing the pygame library.
import pygame

#Initializing pygame.
pygame.init()

#Create a display surface and set its caption.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
#Setting a caption.
pygame.display.set_caption("Drawing objects")