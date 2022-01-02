#Importing a library.
import pygame

#Initializing pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
#Creating display durface.
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Setting the mode of the window.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Creating images, returns a surface object.
dragon_left_image = pygame.image.load("dragon_left.png")
#Creating a rectangle.
dragon_left_rect = dragon_left_image.get_rect()
#Creating images, returns a surface object.
dragon_right_center_image = pygame.image.load("dragon_right_center.png")
#Creating a rectangle.
dragon_right_center_rect = dragon_right_center_image.get_rect()
#Positioning the image.
dragon_right_center_rect.topright = (1300,0)
#Creating images, returns a surface object.
dragon_right_image = pygame.image.load("dragon_right.png")
#Creating a rectangle.
dragon_right_rect = dragon_right_image.get_rect()
#Positioning the image.
dragon_right_rect.topright = (1800,0)

#Positioning the image.
dragon_left_rect.topleft = (0,0)
#Creating images, returns a surface object.
dragon_left_center_image = pygame.image.load("dragon_left_center.png")
#Creating a rectangle.
dragon_left_rect = dragon_left_image.get_rect()
#Creating a rectangle.
dragon_left_center_rect = dragon_left_center_image.get_rect()
dragon_left_center_rect.topleft = (500,0)
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
#Delaying the sound by 5 seconds (5000 milliseconds)
pygame.time.delay(5000) 

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
system_text = system_font.render("Dragons Barrage", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Define the text.
custom_text = system_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = system_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)
#Adding a text render.
custom_text = custom_font.render("By Matthew Ivezaj", True, GREEN)
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
        #Setting a place counter.
        place_counter = 0
        #Checking if the place_counter is equal to 1.
        if place_counter == 1:
            #Stopping the music.
            pygame.mixer.music.stop()
        #Adding 1 to the place counter.
        place_counter = place_counter + 1

    #Blit (copy) the text surfaces to the display surface.
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)
    #Blit (copy) a surface left object at the given cooridnates to our display.
    DISPLAY_SURFACE.blit(dragon_left_image, dragon_left_rect)
    #Blit (copy) a surface right object at the given cooridnates to our display.
    DISPLAY_SURFACE.blit(dragon_right_image, dragon_right_rect)
    #Blit (copy) a surface right-center object at the given cooridnates to our display.
    DISPLAY_SURFACE.blit(dragon_right_center_image, dragon_right_center_rect)
    #Blit (copy) a surface left-center object at the given cooridnates to our display.
    DISPLAY_SURFACE.blit(dragon_left_center_image, dragon_left_center_rect)
    #Drawing a line.
    pygame.draw.line(DISPLAY_SURFACE, (255, 255, 255), (0, 300), (WINDOW_WIDTH, 300), 4)

    #Updating the display.
    pygame.display.update()


#Ending the game.
pygame.quit()