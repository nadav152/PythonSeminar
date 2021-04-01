import pygame

from constants import *
from piece import Piece


class View:

    def __init__(self, controller):
        self.controller = controller

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                if (col % 2 != 0 and row % 2 != 0) or (col % 2 == 0 and row % 2 == 0):
                    pygame.draw.rect(win, LIGHT_BROWN,
                                     (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE + 1, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        self.draw_board_borders(win)

    def draw_board_borders(self, win):
        pygame.draw.line(win, BLACK, [0, 0], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [0, 0], [HEIGHT, 0], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [0, WIDTH], 8)
        pygame.draw.line(win, BLACK, [HEIGHT, WIDTH], [HEIGHT, 0], 12)

    def draw_board(self, win, board):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    def draw_valid_moves(self, win, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(win, RED,
                               ((col * SQUARE_SIZE + SQUARE_SIZE // 2), (row * SQUARE_SIZE + SQUARE_SIZE // 2)), 25,
                               width=4)
            # pygame.draw.rect(self.win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
