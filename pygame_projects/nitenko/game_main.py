#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
#Setting the mode of the window.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Setting a caption.
pygame.display.set_caption("Blitting Images!")
#Creating a caption.
pygame.display.set_caption("Adding Sounds!")
#Loading the sounds.
sound_1 = pygame.mixer.Sound('Jump.wav')
sound_2 = pygame.mixer.Sound('powerup.wav')

#Playing the sounds.
sound_1.play()
#Delaying the sound by 5 seconds (5000 milliseconds)
pygame.time.delay(5000)
#Playing the other sound.
sound_2.play()
#Delaying the sound by 2 seconds (2000 milliseconds)
pygame.time.delay(2000)
#Changing the volume of the outputted sound.
sound_2.set_volume(.1)
#Playing the other sound.
sound_2.play()
#Delaying the sound by 2 seconds (2000 milliseconds)
pygame.time.delay(2000)
#Changing the volume of the outputted sound.
sound_2.set_volume(.01)
#Playing the other sound.
sound_2.play()
#Delaying the sound by 2 seconds (2000 milliseconds)
pygame.time.delay(2000)

#Loading the pygame.mixer and playing background music.
pygame.mixer.music.load("background_music.wav")
#Playing the background music.
"""
Starting at -1 so it plays repeatedly, nonstop.
"""
pygame.mixer.music.play(-1)
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