import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (181, 37, 24)
BLUE = (40, 49, 168)
GREEN = (40, 110, 37)
GRID = (62, 73, 77)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 30

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = BLACK

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
