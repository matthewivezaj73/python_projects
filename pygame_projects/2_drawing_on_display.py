#Importing the pygame library.
import pygame

#Initializing pygame.
pygame.init()

#Create a display surface and set its caption.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
#Displaying a surface and assigning it to a variable.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Setting a caption.
pygame.display.set_caption("Drawing objects")

#Defining colors as RGB tuples.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Giving a background color to the display.
display_surface.fill(BLUE)
#Drawing shapes on the display.
"""
Line(surface, color, stating point, ending point,thickness)
"""
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 5)
"""
Circle(surface, color, center, radius, thickness...0 for fill)
"""
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
#Drawing another circle.
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0)
"""
"""

#Setting a flag.
running = True
#Starting a while loop
while running:
    #Running through each event in event.
    for event in pygame.event.get():
        #Printing the events.
        print(event)
        #Checking if the event types happening are equal to what is happening in pygame.
        if event == pygame.QUIT:
            running = False
    #Updating the display.
    pygame.display.update()

#Ending the game.
pygame.quit()