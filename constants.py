import pygame

WIDTH, HEIGHT = 650, 650
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

MINUTES_PER_PLAYER = 20

RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
BLACK = (36, 34, 34)
BLUE = (0, 77, 230)
DARK_BLUE = (20, 44, 82)
GREY = (217, 213, 204)
DARK_GREY =(92, 92, 61)
BROWN = (153, 102, 51)
LIGHT_BROWN = (255, 204, 102)

CROWN = pygame.transform.scale(pygame.image.load('Assets/crown.png'), (35, 35))
INSTRUCTIONS = pygame.transform.scale(pygame.image.load('Assets/Instructions.jpg'), (705, 494))
EXIT = pygame.transform.scale(pygame.image.load('Assets/cancel.png'), (30, 30))
