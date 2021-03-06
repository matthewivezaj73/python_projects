#Importing the library.
import pygame

#Initialize pygame.
pygame.init()

#Creating a display surface.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#Creating a display surface.
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
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
#Setting a flag.
not_done = False
#Testing for the user to quit the game.
while not not_done:
    #Creating the for loop.
    for event in pygame.event.get():
        #If the event is QUIT, then we will exit the loop.
        if event == pygame.QUIT:
            #Setting the flag to true.
            not_done = True
    # #Updating the game.
    pygame.display.update()
#Quitting the game.
pygame.quit()