#Importing the pygame lib.
import pygame
import pygame.key

#Initializing the pygame.
pygame.init()
#Creating the dimensions of the display.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating the display.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Adding a caption.
pygame.display.set_caption("Discrete Movement!")

#Creating a game value.
VELOCITY = 10

#Load in images.
dragon_image = pygame.image.load("dragon_right.png")
#Creating a rectangle to hold the image.
dragon_rect = dragon_image.get_rect()
#Centering the dragon.
dragon_rect.centerx = WINDOW_WIDTH//2
#Setting the rect height at the bottom.
dragon_rect.bottom = WINDOW_HEIGHT
#Setting a flag.
not_running = False
#The main game loop.
while not not_running:
    #Starting a for loop.
    for event in pygame.event.get():
        #Printing out the events.
        print(event)
        #If the event is a pygame QUIT type.
        if event.type == pygame.QUIT:
            #Setting flag to true to break out of the loop.
            not_running = True

        #Checking for discrete movement.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            elif event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            elif event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            elif event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
    #Blit (Copy) assets to the screen.
    display_surface.blit(dragon_image, dragon_rect)

    #Updating the display.
    pygame.display.update()
#Ending the game.
pygame.quit()