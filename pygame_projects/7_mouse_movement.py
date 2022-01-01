#Importing the pygame lib.
import pygame
#Initializing pygame.
pygame.init()

#Creating parameters of the game surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating a display surface.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Setting a caption.
pygame.display.set_caption("Mouse Movement!")

#Load images.
hero_image = pygame.image.load("hero.png")
#Creating a rect for the hero image.
hero_rect = hero_image.get_rect()
#Positioning the hero rect.
hero_rect.top_left = (25,25)
#Enabling movement of the object with the mouse.
#Setting a flag.
not_running = False
#Testing for user interaction.
while not not_running:
    #Creating a for loop to grab each event that happens.
    for event in pygame.event.get():
        print(event)
        #Checking if the user wants to quit the game.
        if event.type == pygame.QUIT:
            #Changing the flag to get out of the loop.
                not_running = True
    #Filling the display.
    display_surface.fill((0, 0, 0))

    #Blitting the assets.
    display_surface.blit(hero_image, hero_rect)

    #Updating the display.

    #Updating the display.
    pygame.display.update()
#Calling pygame.quit() to exit the game.
pygame.quit()