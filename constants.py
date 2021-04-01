import pygame

WIDTH, HEIGHT = 650, 650
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
BLACK = (36, 34, 34)
BLUE = (0, 0, 255)
GREY = (217, 213, 204)
BROWN = (153, 102, 51)
LIGHT_BROWN = (255, 204, 102)

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (35, 35))
