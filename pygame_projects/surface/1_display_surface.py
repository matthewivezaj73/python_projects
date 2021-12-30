#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating the display surface and setting captions.

#Example from pygame.org
# flags = pygame.OPENGL | pygame.FULLSCREEN
# window_surface = pygame.display.set_mode((1920, 1080), flags, vsync=1)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])