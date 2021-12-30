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

#Defining colors as RGB tuples.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Setting a flag.
not_running = False
#Starting a while loop
while not not_running:
    #Running through each event in event.
    for event in pygame.event.get():
        #Checking if the event types happening are equal to what is happening in pygame.
        if event.type == pygame():
            #Set a flag to true.
            not_running = True

#Ending the game.