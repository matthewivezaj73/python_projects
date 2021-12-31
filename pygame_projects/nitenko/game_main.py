#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
#Setting the mode of the window.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Setting a caption.
pygame.display.set_caption("Blitting Images!")

#Defining colors.
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

#See all available system fonts.
fonts = pygame.font.get_fonts()
#looping through the list of fonts.
for font in fonts:
    print(font)

#Defining fonts.
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font("AttackGraffiti.otf", 32)
#Define the text.
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Define the text.
custom_text = system_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = system_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)
#Adding a text render.
custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
#Setting a flag.
not_running = False
#The main game loop.
while not not_running:
    #Looping through the list of events.
    for event in pygame.event.get():
        #Adding the if in case the user wants to quit.
        if event.type == pygame.QUIT:
            #Setting the flag to true.
            not_running = True

    #Blit (copy) the text surfaces to the display surface.
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)
    #Updating the display.
    pygame.display.update()


#Ending the game.
pygame.quit()