import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
canvas = pygame.display.set_mode([500, 600])
canvas.fill(RED)
pygame.display.flip()
canvas
red_block = pygame.Surface([50, 20])
red_block