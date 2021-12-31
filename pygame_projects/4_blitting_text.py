#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Setting the mode of the window.
display_surface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

#Setting a caption.
pygame.display.set_caption("Blitting Images!")

#Setting a flag.
not_running = False
#The main game loop.
while not not_running:
    #Looping through the list of events.
    for event in pygame.event.get():
        #Setting the flag to true.
        not_running = True