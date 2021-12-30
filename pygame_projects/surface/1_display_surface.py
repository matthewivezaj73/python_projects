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

pygame.display.set_caption("Hello world!")
#Creating a flag.
not_looping = False
#The main loop for the game
while not not_looping:
    #Looping through a list of event objects that have occurred.
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            #Setting not_looping to true so we can break out of the game when the user clicks exit.
            not_looping = True