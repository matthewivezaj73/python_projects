#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
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
#Setting a flag.
not_running = False
#The main game loop.
while not not_running:
    #Looping through the list of events.
    for event in pygame.event.get():
        #Setting the flag to true.
        not_running = True
    #Updating the display.
    pygame.display.update()


#Ending the game.
pygame.quit()