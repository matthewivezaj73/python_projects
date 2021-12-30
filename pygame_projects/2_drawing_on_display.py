#Importing the pygame library.
import pygame

#Initializing pygame.
pygame.init()

#Create a display surface and set its caption.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
#Displaying a surface and assigning it to a variable.
display_surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
#Setting a caption.
pygame.display.set_caption("Drawing objects")

#Setting a flag.
not_running = False
#Starting a while loop
while not not_running:
    for event in pygame.event.get()