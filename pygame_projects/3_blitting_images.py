#Importing pygame.
import pygame
#Initialize pygame.
pygame.init()
#Create a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#Creating images, returns a surface object.
dragon_left_image = pygame.image.load("dragon_left.png")
#Creating a rectangle.
dragon_left_rect = dragon_left_image.get_rect()
#Positioning the image.
dragon_left_rect.topleft = (0,0)
#Creating images, returns a surface object.
dragon_right_image = pygame.image.load("dragon_right.png")
#Creating a rectangle.
dragon_right_rect = dragon_right_image.get_rect()
#Positioning the image.
dragon_right_rect.topright = (WINDOW_WIDTH,0)
#The main game loop.
not_running = False
#Testing for reaction.
while not not_running:
    #Starting a for loop.
    for event in pygame.event.get():
        #If the user selects to quit.
        if event.type == pygame.QUIT:
            #Setting the flag to true.
            not_running = True

    #Blit (copy) a surface object at the given cooridnates to our display.
    DISPLAY_SURFACE.blig(dragon_left_image, dragon_left_rect)
    #Updating the display.
    pygame.display.update()
#End the game.
pygame.quit()