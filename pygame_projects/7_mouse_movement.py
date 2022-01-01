#Importing the pygame lib.
import pygame
#Initializing pygame.
pygame.init()

#Creating parameters of the game surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating a display surface.
display_surface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
#Setting a caption.
pygame.display.set_caption("Mouse Movement!")

#Load images.
hero_image = pygame.image.load("hero.png")
#Setting a flag.
not_running = False
#Testing for user interaction.
while not not_running:
    #Creating a for loop to grab each event that happens.
    for event in pygame.event.get():
        #Checking if the user wants to quit the game.
        if event.type == pygame.QUIT:
            #Changing the flag to get out of the loop.
                not_running = True

#Calling pygame.quit() to exit the game.
pygame.quit()