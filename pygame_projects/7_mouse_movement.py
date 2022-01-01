#Importing the pygame lib.
import pygame
#Initializing pygame.
pygame.init()

#Creating parameters of the game surface.
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 1200
#Creating a display surface.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Setting a caption.
pygame.display.set_caption("Mouse Movement!")

#Load images.
hero_image = pygame.image.load("hero.png")
#Creating a rect for the hero image.
hero_rect = hero_image.get_rect()
#Positioning the hero rect.
hero_rect.topleft = (25,25)
#Enabling movement of the object with the mouse.
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

        #Moving based on mouse clicks.
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Printing the events to monitor on screen.
            print(event)
            #Added an x coordinate.
            mouse_x = event.pos[0]
            #Added an y coordinate. 
            mouse_y = event.pos[1]
            #Adding the rect for the x coordinate.
            hero_rect.centerx = mouse_x
            #Adding the rect for the y coordinate.
            hero_rect.centery = mouse_y
        #Dragging the object when the mouse button is clicked.
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            #Printing the events to monitor on screen.
            print(event)
            #Added an x coordinate.
            mouse_x = event.pos[0]
            #Added an y coordinate. 
            mouse_y = event.pos[1]
            #Adding the rect for the x coordinate.
            hero_rect.centerx = mouse_x
            #Adding the rect for the y coordinate.
            hero_rect.centery = mouse_y
    #Filling the display.
    display_surface.fill((0, 0, 0))

    #Blitting the assets.
    display_surface.blit(hero_image, hero_rect)

    #Updating the display.
    pygame.display.update()
#Calling pygame.quit() to exit the game.
pygame.quit()