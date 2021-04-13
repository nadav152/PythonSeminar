import pygame
from constants import BLACK, SQUARE_SIZE, GREY, CROWN


class Piece:
    PADDING = 14
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw_piece(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        if self.color == BLACK:
            pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        else:
            pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, (self.y - 1) - CROWN.get_height() // 2))

    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


